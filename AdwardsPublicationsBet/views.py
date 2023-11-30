from django.shortcuts import render
from rest_framework import generics
from AdwardsPublicationsBet import serializer

from AdwardsPublicationsBet.models import AdwardsPublicationsBet
import datetime
# Consulta Y Creacion de Campeonatos
class AdwardsPublicationsBetAPIView(generics.ListCreateAPIView):
    queryset = AdwardsPublicationsBet.objects.all()
    serializer_class = serializer.AdwardsPublicationsBetSerializer

