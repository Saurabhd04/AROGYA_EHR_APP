from django.urls import path, include

from . import views

urlpatterns = [
    # path('rest-auth/', include('rest_auth.urls')),
    path('PerInfo/', views.PersonalInfoList.as_view()),
    path('EmergencyInfo/', views.EmergencyInfoList.as_view()),
    path('InsuranceInfo/', views.InsuranceInfoList.as_view()),
    path('PrescriptionInfo/', views.PrescriptionInfoList.as_view()),
    path('OrganizationInfo/', views.OrganizationInfoList.as_view()),
    path('OrganizationInfo/<int:pk>/', views.OrganizationInfoDetail.as_view()),
    path('MedicalPractitionerInfo/', views.MedicalPractitionerInfoList.as_view()),
    # path('PerInfo/', include('PersonalInfo.urls')),
    # path('Register/', include('rest_auth.registration.urls')),
  
]
