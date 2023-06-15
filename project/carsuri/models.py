from django.db import models

class Detail(models.Model):
    detail_no = models.AutoField(primary_key=True)
    detail_name = models.CharField(max_length=255, blank=True, null=True)
    model_num = models.ForeignKey('Model', models.DO_NOTHING, db_column='model_num', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detail'


class Fileupload(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

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