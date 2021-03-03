from django.urls import path

from fitfarmer import views

urlpatterns = [
    path('', views.get_details, name='index'),
   
]