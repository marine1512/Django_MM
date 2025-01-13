from django.db import models
from django.db.models.functions import Now


class Media(models.Model):
    nom = models.fields.CharField(max_length=150)
    type = models.fields.CharField(max_length=150)


class Membre(models.Model):
    nom = models.fields.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    date_inscription = models.DateTimeField(db_default=Now())
