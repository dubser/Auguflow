# Generated by Django 3.0.2 on 2020-01-21 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flow', '0005_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenParams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param_name', models.CharField(max_length=200)),
            ],
        ),
    ]
