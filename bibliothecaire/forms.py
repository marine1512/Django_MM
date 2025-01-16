from django import forms

class Creationmedia(forms.Form):
    type_choices = [
        ('In stock', 'In stock'),
        ('Out of stock', 'Out of stock'),
    ]
    nom = forms.CharField(required=False)
    type = forms.ChoiceField(
        choices=type_choices,
        widget= forms.Select(attrs={
        'class': 'form-control'

    })
    )


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

