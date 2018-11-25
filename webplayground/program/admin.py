from django.contrib import admin
from .models import Lenguajes
from .models import Temas
from .models import Ejercicios

# Register your models here.
admin.site.register(Lenguajes)
admin.site.register(Temas)
admin.site.register(Ejercicios)