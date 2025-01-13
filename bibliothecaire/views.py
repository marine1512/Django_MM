from django.shortcuts import render
from bibliothecaire.forms import Creationmedia
from bibliothecaire.forms import Creationmembre
from bibliothecaire.models import Media, Membre


def listemedias(request):
    medias = Media.objects.all()
    return render(request, 'media/listsMedia.html',
                  {'medias': medias})


def ajoutmedia(request):
    if request.method == 'POST':
        creationmedia = Creationmedia(request.POST)
        if creationmedia.is_valid():
            media = Media()
            media.nom = creationmedia.cleaned_data['nom']
            media.type= creationmedia.cleaned_data['type']
            media.save()
            medias = Media.objects.all()
            return render(request, 'media/listsMedia.html',
                          {'medias': medias})
    else:
        creationmedia = Creationmedia()
        return render(request,
                      'media/ajoutmedia.html',
                      {'creationMedia': creationmedia}
                      )

def listemembres(request):
    membre = Membre.objects.all()
    return render(request, 'membre/membre.html',
                    {'membre': Membre})

def ajoutmembre(request):
    if request.method == 'POST':
        creationmembre = Creationmembre(request.POST)
        if creationmembre.is_valid():
            membre = Membre()
            membre.nom = creationmembre.cleaned_data['nom']
            membre.email = creationmembre.cleaned_data['email']
            membre.date_inscription = creationmembre.cleaned_data['date_inscription']
            membre.save()
            membres = Membre.objects.all()
            return render(request, 'membre/membre.html',
                          {'membres': membres})
    else:
        creationmembre = Creationmembre()
        return render(request,
                      'membre/ajoutmembre.html',
                      {'creationMembre': creationmembre}
                      )