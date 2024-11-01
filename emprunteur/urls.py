from django.urls import path
from . import views

app_name = 'emprunteur'

urlpatterns = [
    path('liste_medias/', views.liste_medias, name='liste_medias'),
    path('', views.home, name='home'),

]
