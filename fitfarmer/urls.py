from django.urls import path

from fitfarmer.views import index, UserList, UserAdd ,IntakeAdd,IntakeList
urlpatterns = [
    path('', index, name='index'),
    path('users/', UserList.as_view()),
    path('register/', UserAdd.as_view()),
    path('intake/',IntakeAdd.as_view()),
    path('foodlist/',IntakeList.as_view())
]