from django.db import models

class Championship(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name', null= False)
    sport = models.IntegerField(verbose_name='Sport', null= False)
    initialDate = models.DateField(verbose_name='Initial Date', null= False)
    finalDate = models.DateField(verbose_name='Final Date', null= False)
    category = models.IntegerField(verbose_name='Category', null= False)
    description = models.TextField(verbose_name='Description', null= False)
  
    class Meta:
        verbose_name = "Championship"
        verbose_name_plural = "Championship"
        db_table = "championship"
        
    def __str__(self):
        return

    def __unicode__(self):
        return
        
