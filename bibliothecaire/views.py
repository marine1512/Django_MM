from django.shortcuts import render
from bibliothecaire.forms import Creationmedia, Creationemprunt, Modifemprunt
from bibliothecaire.forms import Creationmembre
from bibliothecaire.models import Media, Membre, Emprunt


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
                      {'creationMedia': creationmedia})



def listemembres(request):
    membres = Membre.objects.all()
    return render(request, 'membre/membre.html',
                    {'membres': membres})


def ajoutmembre(request):
    if request.method == 'POST':
        creationmembre = Creationmembre(request.POST)
        if creationmembre.is_valid():
            membre = Membre()
            membre.nom = creationmembre.cleaned_data['nom']
            membre.email = creationmembre.cleaned_data['email']
            membre.save()
            membres = Membre.objects.all()
            return render(request,
                          'membre/membre.html',
                          {'membres': membres})
    else:
        creationmembre = Creationmembre()
        return render(request,
                      'membre/ajoutmembre.html',
                      {'creationMembre': creationmembre}
                      )


def ajoutemprunt(request):
    if request.method == 'POST':
        creationemprunt = Creationemprunt(request.POST)
        if creationemprunt.is_valid():
            emprunt = Emprunt()
            emprunt.nom_media = creationemprunt.cleaned_data['nom_media']
            emprunt.type_media= creationemprunt.cleaned_data['type_media']
            emprunt.emprunt = creationemprunt.cleaned_data['emprunt']
            emprunt.save()
            emprunts = Emprunt.objects.all()
            return render(request,
                          'membre/membre.html',
                          {'emprunts': emprunts})
    else:
        creationemprunt = Creationemprunt()
        return render(request,
                      'membre/ajoutemprunt.html',
                      {'creationEmprunt': creationemprunt}
                      )


def modifemprunt(request):
    if request.method == 'POST':
        modif_emprunt = Modifemprunt(request.POST)
        if modif_emprunt.is_valid():
            modif_emprunt = Membre()
            modif_emprunt.nom = modif_emprunt.cleaned_data['nom']
            modif_emprunt.media = modif_emprunt.cleaned_data['media']
            modif_emprunt.membre_emprunt = modif_emprunt.cleaned_data['membre']
            modif_emprunt.save()
            emprunts = Membre.objects.all()
            return render(request,
                        'membre/membre.html',
                        {'emprunts': emprunts})
    else:
        modif_emprunt = Modifemprunt()
        return render(request,
                    'membre/modifemprunt.html',
                    {'modif_Emprunt': modif_emprunt}
                    )