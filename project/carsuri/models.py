from django.db import models

# Create your models here.
class Maker(models.Model):
    maker_no = models.IntegerField(primary_key=True)
    maker_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maker'


class Model(models.Model):
    model_no = models.IntegerField(primary_key=True)
    model_name = models.CharField(max_length=50)
    maker_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'model'


class ModelDetail(models.Model):
    detail_no = models.AutoField(primary_key=True)
    detail_name = models.CharField(max_length=50)
    model_num = models.IntegerField()
    detail_year = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'model_detail'
