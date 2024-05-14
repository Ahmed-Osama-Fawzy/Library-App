from django.urls import path
from . import views

urlpatterns = [
    path("", views.MainHome , name='MainHome'),
    path("LogIn/", views.LogIn , name='LogIn'),
    path("SignUp/", views.SignUp , name='SignUp'),
]