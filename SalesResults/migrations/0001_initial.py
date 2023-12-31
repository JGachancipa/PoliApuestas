# Generated by Django 4.2.7 on 2023-11-30 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalesResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=50, verbose_name='Event')),
                ('description', models.CharField(max_length=50, verbose_name='Description')),
                ('unitValue', models.IntegerField(verbose_name='UnitValue')),
                ('participantsNumber', models.IntegerField(verbose_name='ParticipantsNumber')),
                ('totalValue', models.IntegerField(verbose_name='TotalValue')),
            ],
            options={
                'verbose_name': 'SalesResults',
                'verbose_name_plural': 'SalesResults',
                'db_table': 'salesResults',
            },
        ),
    ]
