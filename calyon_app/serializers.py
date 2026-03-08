# calyon_app/serializers.py
from rest_framework import serializers

class PressureCalcSerializer(serializers.Serializer):
    te_c = serializers.FloatField(required=True, help_text="Evaporation Temp (C)")
    tc_c = serializers.FloatField(required=True, help_text="Condensing Temp (C)")

