from django.shortcuts import render
import MySQLdb
from carsuri.models import Maker, Model, Detail
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
import random

def predict_images(model_path, image_folder):
    # 모델 로드
    model = keras.models.load_model(model_path)
    # 클래스 맵핑 설정
    class_mapping = {
        0: 'Front bumper_s',
        1: 'Front_bumper_c',
        2: 'Side mirror_c',
        3: 'Side mirror_s',
        4: 'Wheel_c',
        5: 'Wheel_s'
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

        base_directory = settings.MEDIA_ROOT
        folder_name = create_folder(base_directory)
        print('11111111111111111',folder_name)

        image_files = request.FILES.getlist('image')
        for image_file in image_files:
            processed_image = process_image(image_file)
            image_path = os.path.join(settings.MEDIA_ROOT, folder_name, image_file.name)
            file_path = default_storage.save(image_path, image_file)
            print(file_path)

        with open(folder_name, 'wb') as file:
            for chunk in processed_image.chunks():
                file.write(chunk)

            # 모델 파일 경로와 이미지 폴더 경로 설정
            model_path = os.path.join('c:/Users/ii818/git/surinam3/project/carsuri/cnnModel3.h5')
            image_folder = os.path.join(settings.MEDIA_ROOT, folder_name)
            
            # 함수 호출하여 예측 수행
            results = predict_images(model_path, image_folder)
            
            print(results)
            print('---------')
            car_json = process_results(results, folder_name)
            print(car_json)
        return render(request, 'predict.html', {'results': car_json})
    else:

        datas = Maker.objects.all()
        return render(request, 'main.html', {'maker':datas})
    
def ModelFunc(request):
    makerId=request.GET.get('makerId')
    car_Model = Model.objects.filter(maker_num=makerId.replace("maker", ""))
    serialized_data = serializers.serialize('json', car_Model)
    data = json.loads(serialized_data)
    return JsonResponse(data, safe=False)

def DetailFunc(request):
    modelId=request.GET.get('modelId')
    model_detail = Detail.objects.filter(model_num=modelId.replace("model", ""))
    serialized_data = serializers.serialize('json', model_detail)
    data = json.loads(serialized_data)
    return JsonResponse(data, safe=False)

def process_image(image_file):
    return image_file

def index(request):
    return render(request, 'bootstrap/index.html')

def create_folder(base_dir):
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    hour = now.strftime("%H")

    random_number = str(random.randint(1000, 9999))

    folder_name = f"{year}{month}{day}{hour}-{random_number}"
    folder_path = os.path.join(base_dir, folder_name)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    return folder_name
