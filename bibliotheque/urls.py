from django.urls import path
from . import views

app_name = "bibliotheque"


urlpatterns = [
    path('membres/', views.liste_membres, name='liste_membres'),
    path('membres/ajouter/', views.ajouter_membre, name='ajouter_membre'),
    path('membres/<int:membre_id>/modifier/', views.mettre_a_jour_membre, name='mettre_a_jour_membre'),
    path('membres/<int:membre_id>/supprimer/', views.supprimer_membre, name='supprimer_membre'),
    path('medias/', views.liste_medias, name='liste_medias'),
    path('medias/ajouter/', views.ajouter_media, name='ajouter_media'),
    path('emprunts/', views.liste_emprunts, name='liste_emprunts'),
    path('emprunts/ajouter/', views.ajouter_emprunt, name='ajouter_emprunt'),
    path('emprunts/<int:emprunt_id>/rentrer/', views.rentrer_emprunt, name='rentrer_emprunt'),
    path('membre/<int:membre_id>/update/', views.update_membre, name='update_membre'),
    path('membre/<int:membre_id>/delete/', views.delete_membre, name='delete_membre'),
    path('', views.home, name='home'),
]
