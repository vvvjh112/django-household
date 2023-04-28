from rest_framework import serializers
from .models import *


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = mainTB
        fields = ( "id","cate1","caption")

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = resultTB
        fields = ( "id","sum1","sum2","sum3","sum4","uid")