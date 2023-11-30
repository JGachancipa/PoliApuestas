from django.db import models

class SalesResults(models.Model):
    
    event = models.CharField(max_length=50, verbose_name='Event', null= False)
    description = models.CharField(max_length=50, verbose_name='Description', null= False)
    unitValue = models.IntegerField(verbose_name='UnitValue', null= False)
    participantsNumber = models.IntegerField(verbose_name='ParticipantsNumber', null= False)
    totalValue = models.IntegerField(verbose_name='TotalValue', null= False)
    
    class Meta:
        verbose_name = "SalesResults"
        verbose_name_plural = "SalesResults"
        db_table = "salesResults"
        
    def __str__(self):
        return

    def __unicode__(self):
        return
