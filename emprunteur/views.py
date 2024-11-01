from django.shortcuts import render
from bibliotheque.models import Livre, DVD, CD, JeuDePlateau


def liste_medias(request):

    livres = Livre.objects.all()
    dvds = DVD.objects.all()
    cds = CD.objects.all()
    jeux_de_plateau = JeuDePlateau.objects.all()
    return render(request, 'emprunteur/liste_medias.html', {
        'livres': livres,
        'dvds': dvds,
        'cds': cds,
        'jeux_de_plateau': jeux_de_plateau
    })

def home(request):
    return render(request, 'emprunteur/home.html')