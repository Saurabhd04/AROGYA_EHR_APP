from rest_framework import serializers
from appV1 import models

# from allauth.account.adapter import get_adapter
# from rest_auth.registration.serializers import RegisterSerializer

# class CustomPerInfoSerializer(RegisterSerializer):
#     AadhaarNumber = serializers.CharField(max_length=12)
#     def get_cleaned_data(self):
#         data_dict = super().get_cleaned_data()
#         data_dict['AadhaarNumber'] = self.validated_data.get('AadhaarNumber', '')
#         return data_dict

class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PersonalInfo
        fields = '__all__'

class EmergencyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EmergencyInfo
        fields = '__all__'

class InsuranceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InsuranceInfo
        fields = '__all__'

class PrescriptionInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PrescriptionInfo
        fields = '__all__'

class OrganizationInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrganizationInfo
        fields = '__all__'

class MedicalPractitionerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MedicalPractitionerInfo
        fields = '__all__'

