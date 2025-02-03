import pytest
from django.test import TestCase
from bibliothecaire.models import Media, Membre, Emprunt



@pytest.fixture
def media(db):
    """Fixture pour créer un media."""
    return Media.objects.create(name="Livre Test", type="Livre", stock=5)


@pytest.fixture
def membre(db):
    """Fixture pour créer un membre."""
    return Membre.objects.create(nom="Test", prenom="User", email="test.user@example.com")


def test_ajout_media(media):
    """Test pour vérifier l'ajout d'un media."""
    assert Media.objects.count() == 1
    assert media.name == "Livre Test"


def test_ajout_membre(membre):
    """Test pour vérifier l'ajout d'un membre."""
    assert Membre.objects.count() == 1
    assert membre.email == "test.user@example.com"


def test_emprunt(db, membre, media):
    """Test pour vérifier la création d'un emprunt."""
    emprunt = Emprunt.objects.create(membre=membre, media=media, retour="2023-10-30")
    assert Emprunt.objects.count() == 1
    assert emprunt.media.name == "Livre Test"

def test_creation_media(media):
    """Vérifie que le média est ajouté correctement."""
    assert Media.objects.count() == 1
    assert media.name == "Livre Test"
    assert media.type == "Livre"
    assert media.stock == 5

def test_creation_membre(membre):
    """Vérifie que le membre est ajouté correctement."""
    assert Membre.objects.count() == 1
    assert membre.nom == "Test"
    assert membre.prenom == "User"
    assert membre.email == "test.user@example.com"

def test_creation_emprunt(db, membre, media):
    """Vérifie que l'emprunt est correctement créé."""
    emprunt = Emprunt.objects.create(membre=membre, media=media, retour="2023-10-30")
    assert Emprunt.objects.count() == 1
    assert emprunt.membre == membre
    assert emprunt.media == media
    assert emprunt.retour == "2023-10-30"