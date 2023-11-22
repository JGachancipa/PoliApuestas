from django.shortcuts import render
from rest_framework import generics
from Sports import serializer

from Sports.models import Championship


class ChampionshipsAPIView(generics.ListCreateAPIView):
    queryset = Championship.objects.all()
    serializer_class = serializer.ChampionshipSerializer


class ChampionshipAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Championship.objects.all()
    serializer_class = serializer.ChampionshipSerializer
