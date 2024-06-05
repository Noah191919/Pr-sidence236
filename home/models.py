from django.db import models

# Create your models here.


class Event(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True)
    type_evenement = models.CharField(max_length=255, null=True, blank=True)
    contenu = models.TextField(null=True, blank=True)
    image = models.ImageField(null = True, blank = True)
    image2 = models.ImageField(null = True, blank = True)
    image3 = models.ImageField(null = True, blank = True)
    date = models.DateTimeField(null = True, blank = True)
    location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return  self.titre 
    
    

class Actu(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True)
    contenu = models.TextField(null=True, blank=True)
    image = models.ImageField(null = True, blank = True)
    image2 = models.ImageField(null = True, blank = True)
    image3 = models.ImageField(null = True, blank = True)
    date = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return  self.titre   
    


class Activite(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True)
    contenu = models.TextField(null=True, blank=True)
    image = models.ImageField(null = True, blank = True)
    date = models.DateTimeField(auto_now=True ,null = True, blank = True)

    def __str__(self):
        return  self.titre 


    
class Album(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True)
    contenu = models.TextField(null=True, blank=True)
    image = models.ImageField(null = True, blank = True)


    def __str__(self):
        return  self.titre
    
    
class Video(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True)
    contenu = models.TextField(null=True, blank=True)
    image = models.ImageField(null = True, blank = True)
    lien = models.CharField(max_length=255, null=True, blank=True) 


    def __str__(self):
        return  self.titre