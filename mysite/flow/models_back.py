from django.db import models

# Create your models here.
class GenParams(models.Model):
    param_name = models.CharField(max_length=200,default=None)
    value= models.CharField(max_length=200,default=None)

    def __str__(self):
        return self.param_name

class pots(models.Model):
     pot_id = models.CharField(max_length=30,default="$")
     note = models.CharField(max_length=200,default="$")
     diametre = models.IntegerField(default=0)
     hauteur = models.IntegerField(default=0)
     longueur = models.IntegerField(default=0)
     largeur = models.IntegerField(default=0)

     def __str__(self):
        return self.note


class espece(models.Model):

     especes_choix = (
     ("Zinnia", "zinnia"),
     ("Tomate", "tomate"),
     ("TomatePM", "tomate PM"),
     ("Capucine", "capucine"),
     ("Autre", "autre"),
)

     especes = models.CharField(max_length=9,choices=especes_choix,
                  default="Autre")

     def __str__(self):
        return self.especes