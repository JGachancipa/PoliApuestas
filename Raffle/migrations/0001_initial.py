# Generated by Django 4.2.7 on 2023-11-27 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Raffle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('participating_number', models.IntegerField()),
                ('maximum_participant', models.IntegerField()),
                ('ticket_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale_start_date', models.DateField()),
                ('sale_end_date', models.DateField()),
                ('game_date', models.DateField()),
                ('main_prize', models.CharField(max_length=200)),
                ('secondary_prize', models.CharField(max_length=200)),
                ('state', models.BooleanField(default=False)),
            ],
        ),
    ]
