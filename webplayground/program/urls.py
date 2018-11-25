from django.urls import path
from .views import LenguajesListView, LenguajesDetailView

program_patterns = ([
    path('', LenguajesListView.as_view(), name='list'),
    path('<nombre_lenguaje>/', LenguajesDetailView.as_view(), name='detail'),
], "program")
