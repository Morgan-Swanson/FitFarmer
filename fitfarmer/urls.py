from django.urls import path

from fitfarmer import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.get_details, name='get-registration'),
    path('register/submit', views.save_details, name='save-registration'),
]