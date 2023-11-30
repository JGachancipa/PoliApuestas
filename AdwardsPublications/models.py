from django.db import models

# Modelo de publicación de premios para la rifa

class AdwardsPublications(models.Model):
    
    #lotteryDate = models.DateField(verbose_name='Lottery Date', null= False)
    raffle = models.CharField(max_length=50, verbose_name='Raffle', null= False)
    date= models.DateField(verbose_name='Date', null= False)
    state= models.CharField(max_length=50, verbose_name='State', null= False)
    winnerNumber= models.IntegerField(verbose_name='WinnerNumber', null= False)
    prize= models.CharField(max_length=50, verbose_name='Prize', null= False)
  
    class Meta:
        verbose_name = "AdwardsPublications"
        verbose_name_plural = "AdwardsPublications"
        db_table = "adwardsPublications"
        
    def __str__(self):
        return

    def __unicode__(self):
        return

    @classmethod
    def estado(cls, state):
        state =cls(state=state)
        '''self.date_now = datetime.datetime.now() 
        self.date = AdwardsPublications.objects.model.date
        self.id = AdwardsPublications.objects.get()
        self.result = AdwardsPublications.objects.model.state'''

        date = AdwardsPublications.objects.model.raffle
        date_now = "Rifa"
        id = AdwardsPublications.objects.model.pk

        for  i in id:
            
            id = AdwardsPublications.objects.get(id=i)
            if  date == date_now:
                result = "Ganó"
            else:
                result = "Perdió"
            i=i+1
        return result