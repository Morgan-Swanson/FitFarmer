from django.urls import path

from fitfarmer.views import index, UserList, UserAdd
urlpatterns = [
    path('', index, name='index'),
    path('users/', UserList.as_view()),
    path('register/', UserAdd.as_view())
]