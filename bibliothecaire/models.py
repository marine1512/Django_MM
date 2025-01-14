from django.db import models


class Media(models.Model):
    nom = models.fields.CharField(max_length=150)
    type = models.fields.CharField(max_length=150)



class Membre(models.Model):
    nom = models.fields.CharField(max_length=150)
    email = models.EmailField()
    emprunt = models.fields.CharField(max_length=150, default='SOME STRING')


"""class Livre(Media):
    name = models.fields.CharField(max_length=150)
    auteur = models.fields.CharField(max_length=150)
    dateEmprunt = ""
    disponible = ""
    emprunteur = models.fields.CharField(max_length=150)


class DVD(Media):
    name = models.fields.CharField(max_length=150)
    realisateur = models.fields.CharField(max_length=150)
    dateEmprunt = ""
    disponible = ""


class CD(Media):
    name = models.fields.CharField(max_length=150)
    artiste = models.fields.CharField(max_length=150)
    dateEmprunt = ""
    disponible = ""
    emprunteur = models.fields.CharField(max_length=150)

class JeuPlateau(models.Model):
    name = models.fields.CharField(max_length=150)
    createur = models.fields.CharField(max_length=150)"""