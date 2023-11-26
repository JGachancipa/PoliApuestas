from django.shortcuts import render
from rest_framework import generics
from Prize import serializer

from Prize.models import Prize


class PrizesAPIView(generics.ListCreateAPIView):
    queryset = Prize.objects.all()
    serializer_class = serializer.PrizeSerializer


class PrizeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prize.objects.all()
    serializer_class = serializer.PrizeSerializer