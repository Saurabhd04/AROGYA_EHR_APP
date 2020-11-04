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

