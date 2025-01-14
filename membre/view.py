from django.shortcuts import render
from bibliothecaire.models import Media


def listemedias(request):
    medias = Media.objects.all()
    return render(request, 'media/listsMedia.html',
                  {'medias': medias})