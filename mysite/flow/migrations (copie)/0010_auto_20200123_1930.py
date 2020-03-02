# Generated by Django 3.0.2 on 2020-01-23 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0009_pots_diametre'),
    ]

    operations = [
        migrations.AddField(
            model_name='pots',
            name='hauteur',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pots',
            name='largeur',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pots',
            name='longueur',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pots',
            name='note',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='pots',
            name='pot_id',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
