from django.urls import path
from bibliothecaire import views

urlpatterns = [
path('', views.listemedias),
path('ajoutmedia/', views.ajoutmedia),
]
