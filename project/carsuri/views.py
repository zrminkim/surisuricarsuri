from django.shortcuts import render
from carsuri.models import Maker, Model, Detail, Map
from django.http import JsonResponse
from django.core import serializers
import json
import os
from django.conf import settings
import numpy as np
from tensorflow import keras
from keras.utils import load_img, img_to_array
from carsuri.car_json import process_results
from django.core.files.storage import default_storage
from datetime import datetime
from django.db.models import Q
from django.core.serializers import serialize
from django.http import HttpResponse

def predict_images(model_path, image_folder):
    # 모델 로드
    model = keras.models.load_model(model_path)
    # 클래스 맵핑 설정
    class_mapping = {
        0: 'Front_bumper_c',
        1: 'Front_bumper_s',
        2: 'Rear_bumper_c',
        3: 'Rear_bumper_s',
        4: 'Side_mirror_c',
        5: 'Side_mirror_s',
        6: 'Wheel_c',
        7: 'Wheel_s',
    }

    # 예측 결과를 저장할 딕셔너리
    predictions = {}

    # 이미지 폴더 내의 파일들에 대해 예측 수행
    for filename in os.listdir(image_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # 이미지 불러오기
            img = load_img(os.path.join(image_folder, filename), target_size=(224, 224))
            img = img_to_array(img)
            img = np.expand_dims(img, axis=0)

            # 예측 수행
            prediction = model.predict(img)
            predicted_class = np.argmax(prediction)

            # 파일이름:분류결과 결과 저장
            predictions[filename] = class_mapping[predicted_class]

    return predictions

# 메인 화면
def MainFunc(request):
    if request.method == 'POST':
        maker_num = request.POST.get('maker_est')
        model_num = request.POST.get('model_est')
        detail_num = request.POST.get('detail_est')
        # print(detail_num)

        base_directory = settings.MEDIA_ROOT
        folder_name = create_folder(base_directory)

        image_files = request.FILES.getlist('image')
        for image_file in image_files:
            processed_image = process_image(image_file)
            image_path = os.path.join(settings.MEDIA_ROOT, folder_name, image_file.name)
            file_path = default_storage.save(image_path, image_file)
            # print(file_path)

        try:
            with open(folder_name, 'wb') as file:
                for chunk in processed_image.chunks():
                    file.write(chunk)
        except:
            # print('file not found : ', file_path)

            # 모델 파일 경로와 이미지 폴더 경로 설정
            # model_path = os.path.join('carsuri/model/cnnModel3.h5')
            # model_path = os.path.join('carsuri/model/cnnModel_4part_0620.h5')
            model_path = os.path.join('carsuri/model/mobilenetV3_4part_gray_edge5_0621.h5')
            image_folder = os.path.join(settings.MEDIA_ROOT, folder_name)
            
            # 함수 호출하여 예측 수행
            results = predict_images(model_path, image_folder)
            # print(results, 'aaaaaaaa')
            car_json = process_results(results, folder_name, maker_num, model_num, detail_num)
            # print(car_json)
        return render(request, 'predict.html', {'results': car_json})
    else:

        datas = Maker.objects.all()
        return render(request, 'main.html', {'maker':datas})
    
    # Maker 버튼을 누르면 Model 버튼을 호출 시키는 매핑작업
def ModelFunc(request):
    makerId=request.GET.get('makerId')
    car_Model = Model.objects.filter(maker_num=makerId.replace("maker", ""))
    serialized_data = serializers.serialize('json', car_Model)
    data = json.loads(serialized_data)
    return JsonResponse(data, safe=False)

    # Model 버튼을 누르면 Detail 버튼을 호출 시키는 매핑작업
def DetailFunc(request):
    modelId=request.GET.get('modelId')
    model_detail = Detail.objects.filter(model_num=modelId.replace("model", ""))
    serialized_data = serializers.serialize('json', model_detail)
    data = json.loads(serialized_data)
    return JsonResponse(data, safe=False)

def process_image(image_file):
    return image_file

    # 이미지 파일 저장 할 때 자동적으로 년/월/일/시/분/1~...번호의 폴더 생성 후 이미지 저장
def create_folder(base_dir):
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    hour = now.strftime("%H")
    minute = now.strftime("%M")

    minute_folder = os.path.join(base_dir, year, month, day, hour, minute)
    last_seq_number = 0

    if os.path.exists(minute_folder):
        subfolders = [f for f in os.listdir(minute_folder) if os.path.isdir(os.path.join(minute_folder, f))]
        last_seq_number = max([int(f) for f in subfolders], default=0)
    
    seq_number = last_seq_number + 1
    
    folder_name = f"{year}/{month}/{day}/{hour}/{minute}/{seq_number}"
    folder_path = os.path.join(base_dir, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_name

def MapFunc(request):

    # center_lat = 37.4987846719974
    # center_lng = 127.031703595662
    southwest_latitude = request.GET.get('swLat')
    southwest_longitude = request.GET.get('swLng')
    northeast_latitude = request.GET.get('neLat')
    northeast_longitude = request.GET.get('neLng')
    
    # 현재 위치 되어 있는 네 곳의 위도 경도 사이의 값만 가져옴 
    result = Map.objects.filter(
        Q(latitude__gte=southwest_latitude) &
        Q(latitude__lte=northeast_latitude) &
        Q(longitude__gte=southwest_longitude) &
        Q(longitude__lte=northeast_longitude)
    )
    json_data = serialize('json', result)

    return HttpResponse(json_data, content_type='application/json')
