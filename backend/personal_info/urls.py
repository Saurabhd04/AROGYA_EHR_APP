from django.urls import path
from . import views


urlpatterns = [
    path('personal-info/', views.PersonalInfoList.as_view()),
]