from django.urls import path
from . import views

urlpatterns = [
    path("" , views.Home , name="Home"),
    path("Borrow/" , views.Borrow , name="Borrow"),
    path("History/" , views.History , name="History"),
    path("Portifloio/" , views.Portifloio , name="Portifloio"),
    path("Logout/" , views.Logout , name="Logout")
]