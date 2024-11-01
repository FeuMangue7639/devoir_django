from django.shortcuts import render, redirect, get_object_or_404
from .models import Membre, Livre, DVD, CD, JeuDePlateau, Emprunt
from django.utils import timezone
from datetime import timedelta


def update_membre(request, membre_id):
    membre = get_object_or_404(Membre, id=membre_id)

    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        adresse = request.POST.get('adresse')


        membre.nom = nom
        membre.email = email
        membre.adresse = adresse


        membre.save()


        return redirect('bibliotheque:liste_membres')


    return render(request, 'bibliotheque/update_membre.html', {'membre': membre})





def home(request):
    return render(request, 'bibliotheque/home.html')



def delete_membre(request, membre_id):
    membre = get_object_or_404(Membre, id=membre_id)
    membre.delete()
    return redirect('bibliotheque:liste_membres')



def liste_membres(request):
    membres = Membre.objects.all()
    return render(request, 'bibliotheque/liste_membres.html', {'membres': membres})


def ajouter_membre(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        Membre.objects.create(nom=nom)
        return redirect('bibliotheque:liste_membres')
    return render(request, 'bibliotheque/ajouter_membre.html')


def mettre_a_jour_membre(request, membre_id):
    membre = get_object_or_404(Membre, pk=membre_id)
    if request.method == 'POST':
        membre.nom = request.POST['nom']
        membre.save()
        return redirect('bibliotheque:liste_membres')
    return render(request, 'bibliotheque/mettre_a_jour_membre.html', {'membre': membre})


def supprimer_membre(request, membre_id):
    membre = get_object_or_404(Membre, pk=membre_id)
    membre.delete()
    return redirect('bibliotheque:liste_membres')



def liste_medias(request):
    livres = Livre.objects.all()
    dvds = DVD.objects.all()
    cds = CD.objects.all()
    jeux_de_plateau = JeuDePlateau.objects.all()
    return render(request, 'bibliotheque/liste_medias.html', {
        'livres': livres,
        'dvds': dvds,
        'cds': cds,
        'jeux_de_plateau': jeux_de_plateau
    })


def ajouter_media(request):
    if request.method == 'POST':
        titre = request.POST.get('titre')
        media_type = request.POST.get('media_type')


        if not titre or not media_type:
            return render(request, 'bibliotheque/ajouter_media.html', {
                'erreur': "Veuillez remplir tous les champs."
            })

        if media_type == 'Livre':
            auteur = request.POST.get('auteur')
            if not auteur:
                return render(request, 'bibliotheque/ajouter_media.html', {
                    'erreur': "Veuillez fournir un auteur."
                })
            Livre.objects.create(titre=titre, auteur=auteur)

        elif media_type == 'DVD':
            realisateur = request.POST.get('realisateur')
            if not realisateur:
                return render(request, 'bibliotheque/ajouter_media.html', {
                    'erreur': "Veuillez fournir un réalisateur."
                })
            DVD.objects.create(titre=titre, realisateur=realisateur)

        elif media_type == 'CD':
            artiste = request.POST.get('artiste')
            if not artiste:
                return render(request, 'bibliotheque/ajouter_media.html', {
                    'erreur': "Veuillez fournir un artiste."
                })
            CD.objects.create(titre=titre, artiste=artiste)

        elif media_type == 'JeuDePlateau':
            # Créez un nouvel objet JeuDePlateau
            JeuDePlateau.objects.create(titre=titre)

        else:
            return render(request, 'bibliotheque/ajouter_media.html', {
                'erreur': "Type de média non valide."
            })

        return redirect('bibliotheque:liste_medias')

    return render(request, 'bibliotheque/ajouter_media.html')



def liste_emprunts(request):
    emprunts = Emprunt.objects.all()
    return render(request, 'bibliotheque/liste_emprunts.html', {'emprunts': emprunts})


def ajouter_emprunt(request):
    if request.method == 'POST':
        membre = Membre.objects.get(pk=request.POST['membre'])
        media_id = request.POST['media']

        # Vérifier le type de média pour récupérer l'objet correspondant
        try:
            media = Livre.objects.get(pk=media_id)
        except Livre.DoesNotExist:
            try:
                media = CD.objects.get(pk=media_id)
            except CD.DoesNotExist:
                media = DVD.objects.get(pk=media_id)

        # Validation de l'emprunt
        if membre.bloque or Emprunt.objects.filter(membre=membre, date_retour__lt=timezone.now()).exists():
            membre.bloque = True
            membre.save()
            return render(request, 'bibliotheque/ajouter_emprunt.html', {
                'erreur': "Ce membre est bloqué en raison d'un emprunt en retard.",
                'membres': Membre.objects.filter(bloque=False),
                'medias': [],  # Aucune média à afficher si le membre est bloqué
            })

        if Emprunt.objects.filter(membre=membre).count() >= 3:
            return render(request, 'bibliotheque/ajouter_emprunt.html', {
                'erreur': "Ce membre a déjà 3 emprunts actifs.",
                'membres': Membre.objects.filter(bloque=False),
                'medias': [],  # Aucun média à afficher si le membre a trop d'emprunts
            })


        date_emprunt = timezone.now()
        date_retour = date_emprunt + timedelta(weeks=1)
        Emprunt.objects.create(membre=membre, media=media, date_emprunt=date_emprunt, date_retour=date_retour)
        return redirect('bibliotheque:liste_emprunts')


    membres = Membre.objects.filter(bloque=False)
    livres = Livre.objects.all()
    cds = CD.objects.all()
    dvds = DVD.objects.all()


    medias = list(livres) + list(cds) + list(dvds)

    return render(request, 'bibliotheque/ajouter_emprunt.html', {'membres': membres, 'medias': medias})


def rentrer_emprunt(request, emprunt_id):
    emprunt = get_object_or_404(Emprunt, pk=emprunt_id)
    emprunt.media.disponible = True
    emprunt.media.save()
    emprunt.delete()
    return redirect('bibliotheque:liste_emprunts')


