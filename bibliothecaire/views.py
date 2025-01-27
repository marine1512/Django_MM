from django.shortcuts import render, get_object_or_404
from bibliothecaire.forms import Creationmedia, Creationemprunt, Modifemprunt
from bibliothecaire.forms import Creationmembre, Modifmembre
from bibliothecaire.models import Media, Membre
from bibliothecaire.models import Emprunt

def index(request):
    return render(request, 'Home.html')
print(index)

def listemedias(request):
    medias = Media.objects.all()
    return render(request, 'media/listsMedia.html',
                  {'medias': medias})


def ajoutmedia(request):
    if request.method == 'POST':
        creationmedia = Creationmedia(request.POST)
        if creationmedia.is_valid():
            media = Media()
            media.name = creationmedia.cleaned_data['name']
            media.type = creationmedia.cleaned_data['type']
            media.stock = creationmedia.cleaned_data['stock']
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


def modifmembre(request, id):
    membre = get_object_or_404(Membre, pk=id)
    if request.method == 'POST':
        modif_membre = Modifmembre(request.POST)
        if modif_membre.is_valid():
            membre.nom = modif_membre.cleaned_data['nom']
            membre.email = modif_membre.cleaned_data['email']
            membre.save()
            updatemembres = Membre.objects.all()
            return render(request,
                        'membre/membre.html',
                        {'membres': updatemembres})
    else:
        modif_membre = Modifmembre()
        return render(request,
                    'membre/modifmembre.html',
                    {'membres': modif_membre}
                    )


def ajoutemprunt(request, id):
    emprunt = get_object_or_404(Media, pk=id)
    if request.method == 'POST':
        creationemprunt = Creationemprunt(request.POST)
        if creationemprunt.is_valid():
            emprunt = Emprunt()
            emprunt.nom_media = creationemprunt.cleaned_data['nom_media']
            emprunt.type_media= creationemprunt.cleaned_data['type_media']
            emprunt.membre_emprunt = creationemprunt.cleaned_data['membre_emprunt']
            emprunt.save()
            membres = Emprunt.objects.all()
            return render(request,
                          'membre/membre.html',
                          {'membres': membres})
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
            emprunt = Membre()
            emprunt.nom = modif_emprunt.cleaned_data['nom']
            emprunt.media = modif_emprunt.cleaned_data['media']
            emprunt.membre_emprunt = modif_emprunt.cleaned_data['membre']
            emprunt.nombre_emprunt = modif_emprunt.cleaned_data['nombre_emprunt']
            emprunt.save()
            membres = Membre.objects.all()
            return render(request,
                        'membre/membre.html',
                        {'membres': membres})
    else:
        modif_emprunt = Modifemprunt()
        return render(request,
                    'membre/modifemprunt.html',
                    {'modif_Emprunt': modif_emprunt}
                    )

