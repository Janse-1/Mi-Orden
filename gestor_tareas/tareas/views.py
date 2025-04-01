from django.shortcuts import render
from rest_framework import viewsets
from .models import Clase, Proyecto, Tarea
from .serializers import ClaseSerializer, ProyectoSerializer, TareaSerializer

class ClaseViewSet(viewsets.ModelViewSet):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

