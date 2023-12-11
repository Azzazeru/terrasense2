from django.db import models

# Create your models here.

class registro_humedad(models.Model):
	idHumedad = models.AutoField(primary_key=True)
	prc_humedad = models.IntegerField()
	fecha_obtencion = models.DateField()
	humedad_ambiente = models.IntegerField()
	temperatura_ambiente = models.IntegerField()


def obtener_ultimo_dato(cls):
        # Obtener el último objeto de TuModelo
        ultimo_dato = cls.objects.last()
        return ultimo_dato