from django.urls import path
from . import views

urlpatterns = [
    path("" , views.Home , name="AHome"),
    path("AddBook/" , views.AddBook , name="AddBook"),
    path("ModifyBook/" , views.ModifyBook , name="ModifyBook"),
    path("RemoveBook/" , views.RemoveBook , name="RemoveBook"),
    path("History/" , views.History , name="AHistory"),
    path("APortifolio/" , views.APortifolio , name="APortifolio"),
    path("ShowBooks/" , views.ShowBooks , name="ShowBooks"),
    path("ShowBook/" , views.ShowBook , name="ShowBook"),
    path("Logout/" , views.Logout , name="ALogout"),
]