from personal_info.models import Personal_info
from rest_framework import serializers



class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal_info
        fields = ["name", "message"]