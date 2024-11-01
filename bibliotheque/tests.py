from django.test import TestCase
from .models import Membre, Livre, Emprunt, DVD, CD, JeuDePlateau

class MembreTestCase(TestCase):
    def setUp(self):
        self.membre = Membre.objects.create(nom="Test Membre")

    def test_membre_creation(self):
        self.assertEqual(self.membre.nom, "Test Membre")

    def test_membre_update(self):
        self.membre.nom = "Membre Mis à Jour"
        self.membre.save()
        self.assertEqual(self.membre.nom, "Membre Mis à Jour")

    def test_membre_delete(self):
        membre_id = self.membre.id
        self.membre.delete()
        with self.assertRaises(Membre.DoesNotExist):
            Membre.objects.get(id=membre_id)

class MediaTestCase(TestCase):
    def setUp(self):
        self.livre = Livre.objects.create(titre="Test Livre", auteur="Auteur Test")
        self.dvd = DVD.objects.create(titre="Test DVD", realisateur="Réalisateur Test")

    def test_livre_creation(self):
        self.assertEqual(self.livre.titre, "Test Livre")
        self.assertEqual(self.livre.auteur, "Auteur Test")

    def test_dvd_creation(self):
        self.assertEqual(self.dvd.titre, "Test DVD")
        self.assertEqual(self.dvd.realisateur, "Réalisateur Test")

class EmpruntTestCase(TestCase):
    def setUp(self):
        self.membre = Membre.objects.create(nom="Test Membre")
        self.livre = Livre.objects.create(titre="Test Livre", auteur="Auteur Test")

    def test_emprunt_creation(self):
        emprunt = Emprunt.objects.create(membre=self.membre, media=self.livre)
        self.assertFalse(emprunt.est_en_retard())

    def test_emprunt_bloque_membre(self):
        Emprunt.objects.create(membre=self.membre, media=self.livre)
        self.membre.bloque = True
        self.membre.save()
        self.assertTrue(self.membre.bloque)

class AjouterMediaTestCase(TestCase):
    def setUp(self):
        self.membre = Membre.objects.create(nom="Membre Test")
        self.livre = Livre.objects.create(titre="Livre Test", auteur="Auteur Test")

    def test_ajouter_media(self):
        self.assertEqual(Livre.objects.count(), 1)
        self.assertEqual(DVD.objects.count(), 0)


        DVD.objects.create(titre="DVD Test", realisateur="Réalisateur Test")
        self.assertEqual(DVD.objects.count(), 1)

class ListeMediasTestCase(TestCase):
    def setUp(self):
        self.livre = Livre.objects.create(titre="Livre Test", auteur="Auteur Test")
        self.dvd = DVD.objects.create(titre="DVD Test", realisateur="Réalisateur Test")
        self.cd = CD.objects.create(titre="CD Test", artiste="Artiste Test")
        self.jeu = JeuDePlateau.objects.create(titre="Jeu Test")

    def test_liste_medias(self):
        response = self.client.get('/medias/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Livre Test")
        self.assertContains(response, "DVD Test")
        self.assertContains(response, "CD Test")
        self.assertContains(response, "Jeu Test")

class JeuDePlateauTestCase(TestCase):
    def setUp(self):
        self.jeu = JeuDePlateau.objects.create(titre="Jeu de Plateau Test")

    def test_jeu_creation(self):
        self.assertEqual(self.jeu.titre, "Jeu de Plateau Test")

class AjouterEmpruntTestCase(TestCase):
    def setUp(self):
        self.membre = Membre.objects.create(nom="Membre Test")
        self.livre = Livre.objects.create(titre="Livre Test", auteur="Auteur Test")
        Emprunt.objects.create(membre=self.membre, media=self.livre)
        Emprunt.objects.create(membre=self.membre, media=self.livre)
        Emprunt.objects.create(membre=self.membre, media=self.livre)

    def test_emprunt_limite(self):
        response = self.client.post('/emprunts/ajouter/', {'membre': self.membre.id, 'media': self.livre.id})
        self.assertContains(response, "Ce membre a déjà 3 emprunts actifs.")
