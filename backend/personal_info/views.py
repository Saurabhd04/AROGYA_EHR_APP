from django.shortcuts import render
from personal_info.models import Personal_info
from personal_info.serializers import PersonalInfoSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.

class PersonalInfoList(APIView):
    
    def get(self, request):
        personal_info = Personal_info.objects.all()
        serializer = PersonalInfoSerializer(personal_info)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonalInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    