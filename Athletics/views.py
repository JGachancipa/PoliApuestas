from django.shortcuts import render
from rest_framework import generics
from Athletics import serializer

from Athletics.models import Athletics

# Consulta Y Creacion de Campeonatos
class AthleticssAPIView(generics.ListCreateAPIView):
    queryset = Athletics.objects.all()
    serializer_class = serializer.AthleticsSerializer

# Actualizacion, Eliminacion y Consulta por ID de Campeonatos 
class AthleticsAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Athletics.objects.all()
    serializer_class = serializer.AthleticsSerializer
