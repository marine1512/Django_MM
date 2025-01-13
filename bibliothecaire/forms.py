from django import forms

class Creationmedia(forms.Form):
    nom = forms.CharField(required=False)
    type = forms.CharField(required=False)

class Creationmembre(forms.Form):
    nom = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    date_inscription = forms.DateTimeField(required=False)