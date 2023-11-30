from django.db import models

# Modelo de publicación de premios para la rifa

class AdwardsPublications(models.Model):
    
    #lotteryDate = models.DateField(verbose_name='Lottery Date', null= False)
    rifa = "Rifa 1"
    fecha= "30/11/2023"
    estado= "gano"
    numeroGanador=23
    premio="premio1"
  
    class Meta:
        verbose_name = "AdwardsPublications"
        verbose_name_plural = "AdwardsPublications"
        db_table = "adwardsPublications"
        
    def __str__(self):
        return

    def __unicode__(self):
        return
