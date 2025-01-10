from django.shortcuts import render
from membre.models import Media


def listemedias(request):
    medias = Media.objects.all()
    return render(request, 'medias/lists.html',
                  {'medias': medias})


