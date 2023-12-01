from django.db import models

class Prize(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name', null= False)
    description = models.CharField(max_length=255,verbose_name='Description', null= False)
    type = models.CharField(max_length=50, verbose_name='Type', null= False)
    value = models.IntegerField(verbose_name='Value', null= False)

    class Meta:
        verbose_name = "Prize"
        verbose_name_plural = "Prize"
        db_table = "prize"
        
    def __str__(self):
        return

    def __unicode__(self):
        return
        
