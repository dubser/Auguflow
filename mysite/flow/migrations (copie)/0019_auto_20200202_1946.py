# Generated by Django 3.0.2 on 2020-02-02 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0018_plant_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plant',
            old_name='Id',
            new_name='PlId',
        ),
    ]
