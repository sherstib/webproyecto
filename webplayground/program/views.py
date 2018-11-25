from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from program.models import Lenguajes


# Create your views here.
class LenguajesListView(ListView):
    model = Lenguajes
    template_name = 'program/lenguajes_list.html'
    paginate_by = 6

class LenguajesDetailView(DetailView):
    model = Lenguajes
    template_name = 'program/lenguajes_list.html'

    def get_object(self):
        return get_object_or_404(Lenguajes, lenguaje_lenguaje=self.kwargs['nombre_lenguaje'])
