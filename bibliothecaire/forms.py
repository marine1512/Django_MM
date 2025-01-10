from django import forms

class Creationmedia(forms.Form):
    nom = forms.CharField(required=False)
    type = forms.CharField(required=False)
    disponible = forms.CharField(required=False)