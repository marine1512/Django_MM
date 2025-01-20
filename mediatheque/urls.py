from django.urls import path
from membre import view
from bibliothecaire import views

urlpatterns = [
    path('', view.listemedias),
    path('media', view.listemedias),
    path('ajoutmedia/', views.ajoutmedia),
    path('ajoutemprunt/', views.ajoutemprunt),
    path('modifemprunt/', views.modifemprunt),
    path('modifmembre/', views.modifmembre),
    path('membre/', views.listemembres),
    path('ajoutmembre/', views.ajoutmembre),
]
