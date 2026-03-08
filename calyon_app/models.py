# calyon_app/models.py
from django.db import models
from django.contrib.auth.models import User

class CalculationHistory(models.Model):  # <-- BURAYI DÜZELTTİK
    """
    PDF Bölüm 27.4: Calculation History
    Kullanıcıların yaptığı hesaplamaları SQL veritabanında saklar.
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    refrigerant = models.CharField(max_length=50, default="Ammonia")
    
    # Girdiler (Inputs)
    evaporation_temperature_c = models.FloatField(help_text="Te (°C)")
    condensing_temperature_c = models.FloatField(help_text="Tc (°C)")
    
    # Çıktılar (Outputs) - Şimdilik sadece basınçlar
    evaporation_pressure_bar = models.FloatField(null=True, blank=True)
    condensing_pressure_bar = models.FloatField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Calc: {self.evaporation_temperature_c}°C / {self.condensing_temperature_c}°C"