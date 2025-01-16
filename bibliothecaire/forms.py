from django import forms

class Creationmedia(forms.Form):
    nom = forms.CharField(required=False)



class Creationmembre(forms.Form):
    nom = forms.CharField(required=False)
    email = forms.EmailField(required=False)


class Creationemprunt(forms.Form):
    nom_media = forms.CharField(required=False)
    type_media = forms.CharField(required=False)
    emprunt = forms.CharField(required=False)


class Modifemprunt(forms.Form):
    nom_media = forms.CharField(required=False)
    type_media = forms.CharField(required=False)
    emprunt = forms.CharField(required=False)

