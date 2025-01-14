from django.urls import path
from bibliothecaire import views

urlpatterns = [
path('', views.listemedias),
path('ajoutmedia/', views.ajoutmedia),
path('ajoutemprunt/', views.ajoutemprunt),
path('modifemprunt/', views.modifemprunt),
path('membre/', views.listemembres),
path('ajoutmembre/', views.ajoutmembre),
]
