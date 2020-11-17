from django.shortcuts import render
from rest_framework.views import APIView
from appV1 import models
from . import serializers
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
#from django.http import HttpResponse
from rest_framework import status
from rest_framework.renderers import HTMLFormRenderer, JSONRenderer, BrowsableAPIRenderer
from django.http import Http404

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

class InsuranceInfoList(APIView):
    serializer_class = serializers.InsuranceInfoSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)
    def get(self, request):
        queryset = models.InsuranceInfo.objects.all()
        serializer = serializers.InsuranceInfoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.InsuranceInfoSerializer(data = request.data)         
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PrescriptionInfoList(APIView):
    serializer_class = serializers.PrescriptionInfoSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)
    def get(self, request):
        queryset = models.PrescriptionInfo.objects.all()
        serializer = serializers.PrescriptionInfoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.PrescriptionInfoSerializer(data = request.data)         
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class OrganizationInfoList(APIView):
    serializer_class = serializers.OrganizationInfoSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)
    def get(self, request):
        queryset = models.OrganizationInfo.objects.all()
        serializer = serializers.OrganizationInfoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.OrganizationInfoSerializer(data = request.data)         
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class OrganizationInfoDetail(APIView):
    serializer_class = serializers.OrganizationInfoSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)
    def get_object(self, pk):
        try:
            return models.OrganizationInfo.objects.get(pk=pk)
        except models.OrganizationInfo.DoesNotExist:
            raise Http404 

    def get(self, request, pk, format=None):
        organization = self.get_object(pk)
        serializer = serializers.OrganizationInfoSerializer(organization)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        organization = self.get_object(pk)
        serializer = serializers.OrganizationInfoSerializer(organization, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                                        

class MedicalPractitionerInfoList(APIView):
    serializer_class = serializers.MedicalPractitionerInfoSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)
    def get(self, request):
        queryset = models.MedicalPractitionerInfo.objects.all()
        serializer = serializers.MedicalPractitionerInfoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.MedicalPractitionerInfoSerializer(data = request.data)         
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)                        