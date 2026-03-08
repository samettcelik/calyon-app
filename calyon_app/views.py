# calyon_app/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CalculationHistory
from CoolProp.CoolProp import PropsSI

class CalculatePressureView(APIView):
    def post(self, request):
        try:
            # 1. Verileri al
            data = request.data
            te_c = float(data.get('te_c'))
            tc_c = float(data.get('tc_c'))


            AMMONIA_CRITICAL_TEMP = 132.25
            
            if tc_c >= AMMONIA_CRITICAL_TEMP:
                return Response({
                    "error": f"HATA: Amonyak için kritik sıcaklık {AMMONIA_CRITICAL_TEMP}°C'dir. "
                             f"Girdiğiniz {tc_c}°C değerinde sıvı/gaz ayrımı yapılamaz (Süperkritik Faz)."
                }, status=status.HTTP_400_BAD_REQUEST)

            if te_c >= AMMONIA_CRITICAL_TEMP:
                return Response({
                    "error": "HATA: Buharlaşma sıcaklığı kritik sıcaklığın üzerinde olamaz."
                }, status=status.HTTP_400_BAD_REQUEST)
            
   
            te_k = te_c + 273.15
            tc_k = tc_c + 273.15
            
            p_evap_pa = PropsSI('P', 'T', te_k, 'Q', 1, 'Ammonia')
            p_evap_bar = p_evap_pa / 100000.0

            p_cond_pa = PropsSI('P', 'T', tc_k, 'Q', 0, 'Ammonia')
            p_cond_bar = p_cond_pa / 100000.0

            CalculationHistory.objects.create(
                evaporation_temperature_c=te_c,
                condensing_temperature_c=tc_c,
                evaporation_pressure_bar=round(p_evap_bar, 3),
                condensing_pressure_bar=round(p_cond_bar, 3)
            )

            return Response({
                "results": {
                    "evaporation_pressure_bar": round(p_evap_bar, 3),
                    "condensing_pressure_bar": round(p_cond_bar, 3)
                }
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)