from django.shortcuts import render
from rest_framework import generics
from SalesResults import serializer

from SalesResults.models import SalesResults

# Consulta Y Creacion de REporte de ventas
class SalesResultsAPIView(generics.ListCreateAPIView):
    queryset = SalesResults.objects.all()
    serializer_class = serializer.SalesResultsSerializer
