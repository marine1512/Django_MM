from django.urls import path
from . import views

app_name="bibliothecaire"
urlpatterns = [
    path('', views.index, name='index'),
    path('listemedias/', views.listemedias, name='listemedias'),
    path('ajoutmedia/', views.ajoutmedia, name='ajoutmedia'),
    path('ajoutemprunt/<int:id>', views.ajoutemprunt, name='ajoutemprunt'),
    path('modifmembre/<int:id>', views.modifmembre, name='modifmembre'),
    path('modifemprunt/<int:id>', views.modifemprunt, name='modifemprunt'),
    path('membre/', views.listemembres, name='listemembres'),
    path('ajoutmembre/', views.ajoutmembre, name='ajoutmembre'),
    path('listeemprunt/<int:id>', views.listeemprunt, name="listeemprunt"),
]
