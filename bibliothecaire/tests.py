from django.test import TestCase
from bibliothecaire.models import Media, Membre, Emprunt


class BibliothequeTests(TestCase):
    def setUp(self):
        self.media = Media.objects.create(name="Livre Test", type="Livre", stock=5)
        self.membre = Membre.objects.create(nom="Test", prenom="User", email="test.user@example.com")

    def test_ajout_media(self):
        self.assertEqual(Media.objects.count(), 1)
        self.assertEqual(self.media.name, "Livre Test")

    def test_ajout_membre(self):
        self.assertEqual(Membre.objects.count(), 1)
        self.assertEqual(self.membre.email, "test.user@example.com")

    def test_emprunt(self):
        emprunt = Emprunt.objects.create(membre=self.membre, media=self.media, retour="2023-10-30")
        self.assertEqual(Emprunt.objects.count(), 1)
        self.assertEqual(emprunt.media.name, "Livre Test")
