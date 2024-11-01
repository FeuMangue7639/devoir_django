from django.db import models
from django.utils import timezone
from datetime import timedelta

class Media(models.Model):
    titre = models.CharField(max_length=100)
    disponible = models.BooleanField(default=True)


    class Meta:
        abstract = False

class Livre(Media):
    auteur = models.CharField(max_length=100)

class DVD(Media):
    realisateur = models.CharField(max_length=100)

class CD(Media):
    artiste = models.CharField(max_length=100)

class JeuDePlateau(models.Model):
    titre = models.CharField(max_length=100)

class Membre(models.Model):
    nom = models.CharField(max_length=100)
    bloque = models.BooleanField(default=False)

class Emprunt(models.Model):
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    date_emprunt = models.DateTimeField(default=timezone.now)
    date_retour = models.DateTimeField(default=timezone.now() + timedelta(days=7))

    def est_en_retard(self):
        return timezone.now() > self.date_retour


