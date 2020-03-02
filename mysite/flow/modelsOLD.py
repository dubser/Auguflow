from django.db import models

# Create your models here.
class Question(models.Model):
    flow_datas = models.CharField(max_length=200)
