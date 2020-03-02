from django.db import models

# Create your models here.
class GenParams(models.Model):
    param_name = models.CharField(max_length=200,default=None)
    value= models.CharField(max_length=200,default=None)

    def __str__(self):
        return str(self.param_nameplant)

class sprayOn(models.Model):
    solenoid_no = models.IntegerField(default=0)


    def __str__(self):
        return str(self.solenoid_no)


class pots(models.Model):
     pot_id = models.CharField(max_length=30,default="$")
     note = models.CharField(max_length=200,default="$")
     diametre = models.IntegerField(default=0)
     hauteur = models.IntegerField(default=0)
     longueur = models.IntegerField(default=0)
     largeur = models.IntegerField(default=0)

     def __str__(self):
        return str(self.note)


class plant(models.Model):

     especes_choix = (
     ("Zinnia", "zinnia"),
     ("Tomate", "tomate"),
     ("TomatePM", "tomate PM"),
     ("Capucine", "capucine"),
     ("Autre", "autre"),
)

     type = models.CharField(max_length=9,choices=especes_choix,
                  default="Autre")
     PlId = models.IntegerField(default=0)
     PotId = models.ForeignKey(pots, on_delete=models.CASCADE, default=1)


     def __str__(self):
         return  ("Plant Id: " + str(self.pk ) + 
         " #" + str(self.PlId ) +" " +str(self.type) )