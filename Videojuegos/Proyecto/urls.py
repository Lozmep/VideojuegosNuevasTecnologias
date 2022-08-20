from django.contrib import admin
from django.urls import path
from LandingPage.views import nombreVista

urlpatterns = [
    path('NombreRuta/', nombreVista),
]
