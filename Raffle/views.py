from rest_framework import viewsets
from .serializer import RaffleSerializer
from .models import Raffle

# Create your views here.
class RaffleView(viewsets.ModelViewSet):
    serializer_class = RaffleSerializer
    queryset = Raffle.objects.all()
