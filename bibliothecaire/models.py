from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Media(models.Model):
    nom = models.fields.CharField(max_length=150)
    type = models.CharField(max_length=150)


class Membre(models.Model):
    nom = models.fields.CharField(max_length=150)
    email = models.EmailField()
    emprunt = models.fields.CharField(max_length=150)
    nombre_emprunt = models.FloatField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(3)
        ]
    )

class Emprunt(models.Model):
    nom_media = models.fields.CharField(max_length=150)
    type_media = models.fields.CharField(max_length=150)


class Livre(Media):
    name = models.fields.CharField(max_length=150)
    auteur = models.fields.CharField(max_length=150)
    emprunteur = models.fields.CharField(max_length=150)


class DVD(Media):
    name = models.fields.CharField(max_length=150)
    realisateur = models.fields.CharField(max_length=150)


class CD(Media):
    name = models.fields.CharField(max_length=150)
    artiste = models.fields.CharField(max_length=150)
    emprunteur = models.fields.CharField(max_length=150)

class JeuPlateau(models.Model):
    name = models.fields.CharField(max_length=150)
    createur = models.fields.CharField(max_length=150)