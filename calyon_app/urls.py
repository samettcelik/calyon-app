# calyon_app/urls.py
from django.urls import path
from .views import CalculatePressureView

urlpatterns = [
    path('calculate/', CalculatePressureView.as_view(), name='calculate_pressure'),
]