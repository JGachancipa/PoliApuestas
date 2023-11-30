from django.db import models

# Modelo de publicación de premios para la apuesta

class AdwardsPublicationsBet(models.Model):
    
    #lotteryDate = models.DateField(verbose_name='Lottery Date', null= False)
    championship = models.CharField(max_length=50, verbose_name='Championship', null= False)
    sport= models.CharField(max_length=50, verbose_name='Sport', null= False)
    date= models.DateField(verbose_name='Date', null= False)
    state= models.CharField(max_length=50, verbose_name='State', null= False)
  
    class Meta:
        verbose_name = "AdwardsPublicationsBet"
        verbose_name_plural = "AdwardsPublicationsBet"
        db_table = "adwardsPublicationsBet"
        
    def __str__(self):
        return

    def __unicode__(self):
        return
