from django.urls import path
from membre import view
from bibliothecaire import views

urlpatterns = [
path('', view.listemedias),
path('ajoutmedia/', views.ajoutmedia),
]
