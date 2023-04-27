from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from . import pds

from .serializers import *
from .models import *
# Create your views here.


class TableList(APIView):
    def get(self, request, path):
        # test = Table.objects
        # pds.test_func("C3456Users56lleel56Desktop56test.db")
        pds.test_func(path)
        test = resultTB.objects
        serializer = ResultSerializer(test, many=True)
        # pds.delete_data()
        return Response(serializer.data)
