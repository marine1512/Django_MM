from django.urls import path
from membre import view
from bibliothecaire import views

urlpatterns = [
path('', view.listemedias),
path('ajoutmedia/', views.ajoutmedia),
path('ajoutemprunt/', views.ajoutemprunt),
path('modifemprunt/<int:id>/', views.modifemprunt),
path('membre/', views.listemembres),
path('ajoutmembre/', views.ajoutmembre),
]
