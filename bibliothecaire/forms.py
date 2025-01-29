from django.utils import timezone
from django import forms
from .models import Media


class Creationmedia(forms.Form):
    type_choices = [
        ('Type', 'Type'),
        ('Livre', 'Livre'),
        ('DVD', 'DVD'),
        ('CD', 'CD'),
        ('Jeu de plateau', 'Jeu de plateau'),
    ]
    stocks = [
        ('Voir', 'Voir'),
        ('Disponible', 'Disponible'),
        ('Indisponible', 'Indisponible'),
    ]

    name = forms.CharField(required=False)
    type = forms.ChoiceField(
        choices=type_choices,
        widget= forms.Select(attrs={
        'class': 'form-control'

    })
    )
    stock = forms.ChoiceField(
        choices=stocks,
        widget= forms.Select(attrs={
        'class': 'form-control'

    })
    )

class Creationmembre(forms.Form):
    nom = forms.CharField(required=False)
    prenom = forms.CharField(required=False)
    email = forms.EmailField(required=False)

class Modifmembre(forms.Form):
    nom = forms.CharField(required=False)
    prenom = forms.CharField(required=False)
    email = forms.EmailField(required=False)


class Creationemprunt(forms.Form):
    media = forms.ChoiceField(required=True,
        choices = [(choice.pk, choice.name + ' (' + choice.type + ')') for choice in Media.objects.all()],
        widget = forms.Select(attrs= {'class': 'form-control'}))

class Modifemprunt(forms.Form):
    nom_media = forms.CharField(required=False)
    type_media = forms.CharField(required=False)
    membre = forms.CharField(required=False)
