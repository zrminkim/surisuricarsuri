from django.db import models
from django.utils import timezone
from uuid import uuid4
import os

class Detail(models.Model):
    detail_no = models.AutoField(primary_key=True)
    detail_name = models.CharField(max_length=255, blank=True, null=True)
    model_num = models.ForeignKey('Model', models.DO_NOTHING, db_column='model_num', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detail'

# 이미지 업로드 파일 저장을 함수로 지정하여 저장
def date_upload_to(instance, filename):
    # upload_to="%Y/%m/%d" 처럼 날짜로 세분화
    ymd_path = timezone.now().strftime('%Y/%m/%d')
    # 길이 32 인 uuid 값
    uuid_name = uuid4().hex
    # 확장자 추출
    extension = os.path.splitext(filename)[-1].lower()
    # 결합 후 return
    return '/'.join([
        ymd_path,
        uuid_name + extension,
    ])

class Fileupload(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to=date_upload_to)

    class Meta:
        managed = False
        db_table = 'fileupload'


class Maker(models.Model):
    maker_no = models.AutoField(primary_key=True)
    maker_name = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maker'


class Model(models.Model):
    model_no = models.AutoField(primary_key=True)
    model_name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    maker_num = models.ForeignKey(Maker, models.DO_NOTHING, db_column='maker_num', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'model'