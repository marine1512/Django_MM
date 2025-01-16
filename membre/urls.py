from django.urls import path
from membre import view

urlpatterns = [
    path('', view.listemedias),
]
