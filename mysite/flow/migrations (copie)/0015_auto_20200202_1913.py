# Generated by Django 3.0.2 on 2020-02-02 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0014_auto_20200124_0014'),
    ]

    operations = [
        migrations.CreateModel(
            name='plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant', models.CharField(choices=[('Zinnia', 'zinnia'), ('Tomate', 'tomate'), ('TomatePM', 'tomate PM'), ('Capucine', 'capucine'), ('Autre', 'autre')], default='Autre', max_length=9)),
            ],
        ),
        migrations.DeleteModel(
            name='espece',
        ),
    ]