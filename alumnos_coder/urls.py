#from curses import curs_set
from unicodedata import name
from django.urls import include, path
from .views import listado_alumnos
from .views import CursoForm




urlpatterns = [
     path('alumnos/',listado_alumnos),
     path('formulario/', CursoForm)
    ]