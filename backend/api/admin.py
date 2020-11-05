from django.contrib import admin

# Register your models here.
from appV1 import models

admin.site.register(models.PersonalInfo)
admin.site.register(models.EmergencyInfo)
admin.site.register(models.InsuranceInfo)
