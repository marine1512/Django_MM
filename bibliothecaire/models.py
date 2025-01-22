from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Membre(models.Model):
    nom = models.fields.CharField(max_length=150)
    email = models.EmailField()
   # emprunt = models.fields.CharField(max_length=150)
    nombre_emprunt = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(3)
        ]
    )
    def __str__(self):
        return self.nom

class Media(models.Model):
    name = models.fields.CharField(max_length=150)
    type = models.CharField(max_length=150)
    stock = models.CharField(max_length=150)


class Livre(Media):
    auteur = models.fields.CharField(max_length=150)
    def __str__(self):
        return self.name+" ('+self.auteur+')"


class DVD(Media):
    realisateur = models.fields.CharField(max_length=150)
    def __str__(self):
        return self.name+" ('+self.realisateur+')"


class CD(Media):
    artiste = models.fields.CharField(max_length=150)
    def __str__(self):
        return self.name+" ('+self.artiste+')"

class Jeuplateau(models.Model):
    name = models.fields.CharField(max_length=150)
    createur = models.fields.CharField(max_length=150)
    def __str__(self):
        return self.name+" ('+self.createur+')"


class Emprunt(models.Model):
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    date_emprunt = models.DateField()
    date_retour = models.DateField()
