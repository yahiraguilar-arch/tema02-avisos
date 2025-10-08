from django.shortcuts import render
from django.utils.timezone import localdate
from django.views.generic.list import ListView
from .models import Aviso

# Create your views here.
class AvisosVigentesListView(ListView):
	model = Aviso
	template_name = "avisos/lista.html" # ruta al template
	context_object_name = "avisos"

	def get_queryset(self):
		hoy = localdate() # fecha actual (aware de zona horaria)
		return (
			Aviso.objects
			.filter(fecha_inicio__lte=hoy, fecha_fin__gte=hoy)
			.order_by('-fecha_inicio')
		)


def landing_page(request):
	return render(request, 'landing.html')