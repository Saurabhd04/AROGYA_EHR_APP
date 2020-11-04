from django.urls import path, include

from . import views

urlpatterns = [
    # path('rest-auth/', include('rest_auth.urls')),
    path('PerInfo/', views.PersonalInfoList.as_view()),
    #path('<int:pk>/', views.DetailTodo.as_view()),
    # path('PerInfo/', include('PersonalInfo.urls')),
    # path('Register/', include('rest_auth.registration.urls')),
  
]
