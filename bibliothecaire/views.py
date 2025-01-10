from django.shortcuts import render
from bibliothecaire.forms import Creationmedia
from bibliothecaire.models import Media


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