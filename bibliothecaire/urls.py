from django.urls import path
from bibliothecaire import views

urlpatterns = [
    path('', views.index),
    path('media/', views.listemedias),
    path('ajoutmedia/', views.ajoutmedia),
    path('ajoutemprunt/', views.ajoutemprunt),
    path('modifmembre/', views.modifmembre),
    path('modifemprunt/', views.modifemprunt),
    path('membre/', views.listemembres),
    path('ajoutmembre/', views.ajoutmembre),
]
