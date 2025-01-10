from django.db import models

class Media(models.Model):
    nom = models.fields.CharField(max_length=150)
    type = models.fields.CharField(max_length=150)
    disponible = models.fields.CharField(max_length=150)
