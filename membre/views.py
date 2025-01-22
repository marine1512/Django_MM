from django.shortcuts import render
from bibliothecaire.models import Media


def listemedias(request):
    medias = Media.objects.all()
    return render(request, 'membre/medias/lists.html',
                  {'medias': medias})