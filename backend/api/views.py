from django.shortcuts import render
from rest_framework.views import APIView
from appV1 import models
from . import serializers
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
#from django.http import HttpResponse
from rest_framework import status
from rest_framework.renderers import HTMLFormRenderer, JSONRenderer, BrowsableAPIRenderer

# Create your views here.
class PersonalInfoList(APIView):
    serializer_class = serializers.PersonalInfoSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)
    def get(self, request):
        queryset = models.PersonalInfo.objects.all()
        serializer = serializers.PersonalInfoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.PersonalInfoSerializer(data = request.data)         
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmergencyInfoList(APIView):
    serializer_class = serializers.EmergencyInfoSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)
    def get(self, request):
        queryset = models.EmergencyInfo.objects.all()
        serializer = serializers.EmergencyInfoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.EmergencyInfoSerializer(data = request.data)         
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)