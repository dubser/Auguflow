# Generated by Django 3.0.2 on 2020-02-02 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0017_auto_20200202_1943'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='Id',
            field=models.IntegerField(default=0),
        ),
    ]
