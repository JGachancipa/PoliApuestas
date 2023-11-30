from django.db import models

class Raffle(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    participating_number = models.IntegerField()
    maximum_participant = models.IntegerField()
    ticket_value = models.DecimalField(max_digits=10, decimal_places=2)
    sale_start_date = models.DateField()
    sale_end_date = models.DateField()
    game_date = models.DateField()
    main_prize = models.CharField(max_length=200)
    secondary_prize = models.CharField(max_length=200)
    state = models.BooleanField(default=False)
    winning_number = models.IntegerField()

    # Agregar la función para visualizar el nombre de la tarea desde el panel administrativo
    def __str__(self):
        return self.title