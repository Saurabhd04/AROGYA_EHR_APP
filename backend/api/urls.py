from django.urls import path, include

from . import views

urlpatterns = [
    
    path('PersonalInfo/', views.PersonalInfoList.as_view()),
    path('PersonalInfoOfSpecificUser/<int:pk>', views.PersonalInfoOfSpecificUser.as_view()), 
    path('EmergencyInfo/', views.EmergencyInfoList.as_view()),
    path('EmergencyInfoOfSpecificUser/<int:fk>', views.EmergencyInfoOfSpecificUser.as_view()),

    path('InsuranceInfo/', views.InsuranceInfoList.as_view()),
    path('InsuranceInfo/<int:pk>', views.InsuranceInfoList.as_view()),
    path('PrescriptionInfo/', views.PrescriptionInfoList.as_view()),
    path('PrescriptionInfoOfSpecificUser/', views.PrescriptionInfoOfSpecificUser.as_view()),

    path('OrganizationInfo/', views.OrganizationInfoList.as_view()),
    path('OrganizationInfo/<int:pk>/', views.OrganizationInfoDetail.as_view()),
    path('MedicalPractitionerInfo/', views.MedicalPractitionerInfoList.as_view()),
    path('MedicalPractitionerInfo/<int:pk>', views.MedicalPractitionerInfoList.as_view()),
    path('MedicalPractitionerInfoOfSpecificOrganization/<int:fk>/', views.MedicalPractitionerInfoOfSpecificOrganization.as_view()),
   
    path('BloodPressure/', views.BloodPressureList.as_view()),
    path('BloodPressure/<int:pk>/', views.BloodPressureDetail.as_view()),
    path('BloodPressureOfSpecificUser/<int:fk>/', views.BloodPressureOfSpecificUser.as_view()),
    path('BodyTemperature/', views.BodyTemperatureList.as_view()),
    path('BodyTemperature/<int:pk>', views.BodyTemperatureDetail.as_view()),
    path('BodyTemperatureOfSpecificUser/<int:fk>/', views.BodyTemperatureOfSpecificUser.as_view()),
    path('HeartRate/', views.HeartRateList.as_view()),
    path('HeartRate/<int:pk>', views.HeartRateDetail.as_view()),
    path('HeartRateOfSpecificUser/<int:fk>/', views.HeartRateOfSpecificUser.as_view()),
    path('RespiratoryRate/', views.RespiratoryRateList.as_view()),
    path('RespiratoryRate/<int:pk>', views.RespiratoryRateDetail.as_view()),
    path('RespiratoryRateOfSpecificUser/<int:fk>/', views.RespiratoryRateOfSpecificUser.as_view()),

    # path('Register/', include('rest_auth.registration.urls')),
  
]
