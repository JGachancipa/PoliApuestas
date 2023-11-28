from django.db import models

# Modelo de Campeonatos
class Athletics(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name', null= False)
    description = models.TextField(verbose_name='Description', null= False)
  
    class Meta:
        verbose_name = "Athletics"
        verbose_name_plural = "Athletics"
        db_table = "athletics"
        
    def __str__(self):
        return

    def __unicode__(self):
        return
        
