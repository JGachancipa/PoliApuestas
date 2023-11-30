from django.shortcuts import render
from rest_framework import generics
from AdwardsPublications import serializer

from AdwardsPublications.models import AdwardsPublications

# Consulta Y Creacion de Campeonatos
class AdwardsPublicationsAPIView(generics.ListCreateAPIView):
    queryset = AdwardsPublications.objects.all()
    serializer_class = serializer.ChampionshipSerializer

# Create your views here.
