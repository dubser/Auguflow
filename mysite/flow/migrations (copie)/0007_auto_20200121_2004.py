# Generated by Django 3.0.2 on 2020-01-21 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0006_genparams'),
    ]

    operations = [
        migrations.AddField(
            model_name='genparams',
            name='value',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='genparams',
            name='param_name',
            field=models.CharField(default=None, max_length=200),
        ),
    ]