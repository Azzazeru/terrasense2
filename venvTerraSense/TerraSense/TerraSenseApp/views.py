from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import registro_humedad

from .models import registro_humedad

# Create your views here.

TEMPLATE_DIRS = (
	'os.path.join(BASE_DIR, "templates"),'
)

def access(request):
	return render(request, "access.html")

def home(request):
	return render(request, "home.html")

def configuration(request):
	return render(request, "configuration.html")

def dataOptionSelector(request):
	return render(request, "functions/dataOptionSelector.html")

def obtener_ultimo_dato(request):
    ultimo_registro = registro_humedad.objects.order_by('-idHumedad').first()
    if ultimo_registro:
        data = {
            'prc_humedad': ultimo_registro.prc_humedad,
            'fecha_obtencion': str(ultimo_registro.fecha_obtencion),
            'humedad_ambiente': ultimo_registro.humedad_ambiente,
            'temperatura_ambiente' : ultimo_registro.temperatura_ambiente
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'No se encontraron datos'})