from django.db import models

# Modelo de Sorteo

class Lottery(models.Model):
    
    lotteryDate = models.DateField(verbose_name='Lottery Date', null= False)
    
  
    class Meta:
        verbose_name = "Lottery"
        verbose_name_plural = "Lottery"
        db_table = "lottery"
        
    def __str__(self):
        return

    def __unicode__(self):
        return
        
