from django.shortcuts import render
from rest_framework import generics
from Lottery import serializer

from Lottery.models import Lottery
import datetime
#import ramdom

# Consulta Y Creacion de sorteo
class LotteryAPIView(generics.ListCreateAPIView):
    queryset = Lottery.objects.all()
    serializer_class = serializer.LotterySerializer
    
    def lottery(self):

        
        self.lottery = Lottery.objects.lotteryDate
        self.now_date=datetime.datetime.now()

        if self.lottery == self.now_date:
            print("si es correcto")
        else:
            print("no es correcto")


#items = list(Product.objects.all())

## change 3 to how many random items you want
#random_items = random.sample(items, 3)
## if you want only a single random item
#random_item = random.choice(items)

