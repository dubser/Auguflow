# Generated by Django 3.0.2 on 2020-02-03 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0006_remove_plant_potid'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='PotId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='flow.pots'),
        ),
    ]
