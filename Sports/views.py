from django.shortcuts import render
from rest_framework import generics
from Sports import serializer

from Sports.models import Championship

# Consulta Y Creacion de Campeonatos
class ChampionshipsAPIView(generics.ListCreateAPIView):
    queryset = Championship.objects.all()
    serializer_class = serializer.ChampionshipSerializer

# Actualizacion, Eliminacion y Consulta por ID de Campeonatos 
class ChampionshipAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Championship.objects.all()
    serializer_class = serializer.ChampionshipSerializer
