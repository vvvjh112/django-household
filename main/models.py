from django.db import models

# Create your models here.


class mainTB(models.Model): #원본 데이터 임시 저장 (근데 할 필요가 있나 싶음)
    id = models.IntegerField(null=False, primary_key=True)
    DATE = models.IntegerField(blank=True, null=True)
    ca1 = models.IntegerField(blank=True, null=True)
    ca2 = models.IntegerField(blank=True, null=True)
    ca3 = models.IntegerField(blank=True, null=True)
    ca4 = models.IntegerField(blank=True, null=True)
    caption = models.TextField(blank=True, null=True)
    uid = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'mainTB'

class resultTB(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    sum1 = models.IntegerField(blank=True, null=True)
    sum2 = models.IntegerField(blank=True, null=True)
    sum3 = models.IntegerField(blank=True, null=True)
    sum4 = models.IntegerField(blank=True, null=True)
    uid = models.IntegerField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'resultTB'