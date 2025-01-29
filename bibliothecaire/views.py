from django.shortcuts import render, get_object_or_404
from bibliothecaire.forms import Creationmedia, Creationemprunt, Modifemprunt
from bibliothecaire.forms import Creationmembre, Modifmembre
from bibliothecaire.models import Media, Membre
from bibliothecaire.models import Emprunt

def index(request):
    return render(request, 'Home.html')

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
            membre.prenom = creationmembre.cleaned_data['prenom']
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
            membre.prenom = modif_membre.cleaned_data['prenom']
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
    membres = Membre.objects.all()
    if request.method == 'POST':
        creationemprunt = Creationemprunt(request.POST)
        if creationemprunt.is_valid():
            encours_emprunts = Emprunt.objects.filter(membre=id).count()
            if encours_emprunts < 3:
                emprunt = Emprunt()
                emprunt.membre = Membre.objects.get(pk=id)
                emprunt.media = Media.objects.get(pk=request.POST['media'])
                emprunt.save()
                return render(request,
                          'membre/membre.html',
                          {'membres': membres, 'message': 'Emprunt créé', 'class': 'success'})
            else:
                return render(request,
                              'membre/membre.html',
                              {'membres': membres, 'message': 'Maximum de 3 emprunts atteint.', 'class': 'error'})
    else:
        creationemprunt = Creationemprunt()
        return render(request,
                'emprunts/ajoutemprunt.html',
                {'creationEmprunt': creationemprunt})




def modifemprunt(request, id):
    emprunt = get_object_or_404(Emprunt, pk=id)
    membre = emprunt.membre
    emprunt.delete()
    emprunts = Emprunt.objects.filter(membre=membre.id)
    return render(request, 'emprunts/emprunt.html', {'emprunts': emprunts})

def listeemprunt(request, id):
    emprunts = Emprunt.objects.filter(membre=id)
    return render(request, 'emprunts/emprunt.html', {'emprunts': emprunts})