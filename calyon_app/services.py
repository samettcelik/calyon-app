# calyon_app/services.py
import logging
from CoolProp.CoolProp import PropsSI

logger = logging.getLogger(__name__)

class ThermodynamicCalculator:
  
    REFRIGERANT = "Ammonia"

    @classmethod
    def calculate_pressures(cls, te_c: float, tc_c: float) -> dict:
        try:
            # 1. Birim Dönüşümleri (PDF Kuralı: CoolProp'a Kelvin gönderilir)
            te_k = te_c + 273.15
            tc_k = tc_c + 273.15

            # Q=1 Saturated Vapor (Doymuş Buhar)
            p_evap_pa = PropsSI('P', 'T', te_k, 'Q', 1, cls.REFRIGERANT)
            p_evap_bar = p_evap_pa / 100000.0  # Pascal to Bar

           
            # Q=0 Saturated Liquid (Doymuş Sıvı)
            p_cond_pa = PropsSI('P', 'T', tc_k, 'Q', 0, cls.REFRIGERANT)
            p_cond_bar = p_cond_pa / 100000.0  # Pascal to Bar

            return {
                "success": True,
                "p_evap_bar": round(p_evap_bar, 3),
                "p_cond_bar": round(p_cond_bar, 3)
            }

        except ValueError as e:
            # CoolProp limit dışı sıcaklıklarda hata fırlatır
            logger.error(f"CoolProp Calculation Error: {str(e)}")
            return {
                "success": False,
                "error": "Sıcaklık değerleri Amonyak faz diyagramı sınırları dışında."
            }