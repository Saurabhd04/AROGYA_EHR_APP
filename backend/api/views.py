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

class EmergencyInfoOfSpecificUser(APIView):
    def get_object(self, fk):
        try:
            return models.EmergencyInfo.objects.filter(userId = fk)
        except models.PrescriptionInfo.DoesNotExist:
            raise Http404

    def get(self, request, fk, format=None):
        queryset = self.get_object(fk)
        serializer = serializers.EmergencyInfoSerializer(queryset, many=True)
        return Response(serializer.data)            

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

class InsuranceInfoOfSpecificUser(APIView):
    def get_object(self, fk):
        try:
            return models.InsuranceInfo.objects.filter(userId = fk)
        except models.InsuranceInfo.DoesNotExist:
            raise Http404

    def get(self, request, fk, format=None):
        queryset = self.get_object(fk)
        serializer = serializers.InsuranceInfoSerializer(queryset, many=True)
        return Response(serializer.data)  

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
            #Checking whether the prescriber is a valid Prescriber
            pid = serializer.validated_data.get("prescriberId")
            ln = models.MedicalPractitionerInfo.objects.get(id = pid.__dict__['id']).__dict__["licenseNumber"]
            if(ln[0:1] == 'D'):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response("You dont have the right to prescribe medicines.")    
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class PrescriptionInfoOfSpecificUser(APIView):
    def get_object(self, fk):
        try:
            return models.PrescriptionInfo.objects.filter(userId = fk, )
        except models.PrescriptionInfo.DoesNotExist:
            raise Http404

    def get(self, request, fk, format=None):
        userPrescriptions = self.get_object(fk)
        serializer = serializers.PrescriptionInfoSerializer(userPrescriptions, many=True)
        return Response(serializer.data)    

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

class MedicalPractitionerInfoOfSpecificOrganization(APIView):
    def get_object(self, fk):
        try:
            return models.MedicalPractitionerInfo.objects.filter(orgId = fk, )
        except models.MedicalPractitionerInfo.DoesNotExist:
            raise Http404

    def get(self, request, fk, format=None):
        medicalPractitioner = self.get_object(fk)
        serializer = serializers.MedicalPractitionerInfoSerializer(medicalPractitioner, many=True)
        return Response(serializer.data)                


class BloodPressureList(APIView):
    serializer_class = serializers.BloodPressureSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)
    def get(self, request):
        queryset = models.BloodPressure.objects.all()
        serializer = serializers.BloodPressureSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.BloodPressureSerializer(data = request.data)         
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      

class BloodPressureDetail(APIView):
    def get_object(self, pk):
        try:
            return models.BloodPressure.objects.get(id = pk)
        except models.BloodPressure.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = serializers.BloodPressureSerializer(queryset)
        return Response(serializer.data)          

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)                  

class BloodPressureOfSpecificUser(APIView):
    def get_object(self, fk):
        try:
            return models.BloodPressure.objects.filter(userId = fk, )
        except models.BloodPressure.DoesNotExist:
            raise Http404

    def get(self, request, fk, format=None):
        queryset = self.get_object(fk)
        serializer = serializers.BloodPressureSerializer(queryset, many=True)
        return Response(serializer.data)           

class BodyTemperatureList(APIView):
    serializer_class = serializers.BodyTemperatureSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)
    def get(self, request):
        queryset = models.BodyTemperature.objects.all()
        serializer = serializers.BodyTemperatureSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.BodyTemperatureSerializer(data = request.data)         
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)          

class BodyTemperatureDetail(APIView):
    def get_object(self, pk):
        try:
            return models.BodyTemperature.objects.get(id = pk)
        except models.BodyTemperature.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = serializers.BodyTemperatureSerializer(queryset)
        return Response(serializer.data)          

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BodyTemperatureOfSpecificUser(APIView):
    def get_object(self, fk):
        try:
            return models.BodyTemperature.objects.filter(userId = fk, )
        except models.BodyTemperature.DoesNotExist:
            raise Http404

    def get(self, request, fk, format=None):
        queryset = self.get_object(fk)
        serializer = serializers.BodyTemperatureSerializer(queryset, many=True)
        return Response(serializer.data)


class HeartRateList(APIView):
    serializer_class = serializers.HeartRateSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)
    def get(self, request):
        queryset = models.HeartRate.objects.all()
        serializer = serializers.HeartRateSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.HeartRateSerializer(data = request.data)         
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)          

class HeartRateDetail(APIView):
    def get_object(self, pk):
        try:
            return models.HeartRate.objects.get(id = pk)
        except models.HeartRate.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = serializers.HeartRateSerializer(queryset)
        return Response(serializer.data)          

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HeartRateOfSpecificUser(APIView):
    def get_object(self, fk):
        try:
            return models.HeartRate.objects.filter(userId = fk, )
        except models.HeartRate.DoesNotExist:
            raise Http404

    def get(self, request, fk, format=None):
        queryset = self.get_object(fk)
        serializer = serializers.HeartRateSerializer(queryset, many=True)
        return Response(serializer.data)          
