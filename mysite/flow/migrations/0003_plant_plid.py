# Generated by Django 3.0.2 on 2020-02-02 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0002_auto_20200202_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='PlId',
            field=models.IntegerField(default=0),
        ),
    ]
