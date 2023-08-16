from . import views
from django.urls import path

urlpatterns = [
    path('', views.weather_forecast, name='weather_forecast')
]
