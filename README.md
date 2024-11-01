Rapport de Projet Django
Hugo COELHO
01/11/2024

a) Introduction

Objectif du Projet:
Le projet vise à moderniser le système de gestion de la médiathèque "Notre livre,
notre média" en créant une application web avec Django. L'objectif est de faciliter la
gestion des emprunts et des membres, d'optimiser l'expérience utilisateur et de
rendre le système plus efficace.

b) Analyse et Correctifs du Code Fourni

Résumé:
Le code initial présentait plusieurs limitations, notamment :
● Manque de Structure Orientée Objet (POO) : Les classes n'étaient pas bien
structurées, ce qui compliquait la maintenance et l'évolution du code.
● Absence de Séparation des Fichiers : Les fichiers contenaient des
méthodes et classes non organisées, rendant la compréhension du code
difficile.

Correctifs Apportés:
Pour remédier à ces problèmes :
● Restructuration des Classes : Les classes Livre, DVD, et CD ont été
restructurées pour hériter d'une classe parent Media, centralisant ainsi les
attributs et méthodes communes.
● Transformation en Application Web Django : L'application a été convertie
en une application web Django avec des modèles bien définis et une structure
de projet organisée. Cela inclut des modèles pour les membres, les emprunts
et les médias.

c) Mise en Place des Fonctionnalités Demandées

Application Bibliothécaire (bibliothèque):
● Gestion des Membres : Ajout, affichage, mise à jour et suppression des
membres.
● Gestion des Emprunts : Les bibliothécaires peuvent gérer les emprunts,
avec des règles telles que :
○ Limite de trois emprunts par membre.
○ Blocage automatique en cas de retard de retour.
● Gestion des Médias : Ajout de nouveaux médias (livres, DVDs, CDs, Jeux
de plateau).
Application Membre
● Consultation des médias : Les membres peuvent consulter la liste des
médias disponibles sans possibilité de modification.

Règles de Gestion:
● Un membre peut emprunter jusqu'à trois médias simultanément.
● Un emprunt doit être retourné dans un délai d'une semaine ; au-delà, le
membre est bloqué.
● Les jeux de plateau ne peuvent pas être empruntés.

d) Stratégie de Tests

Une série de tests unitaires a été mise en œuvre pour chaque fonctionnalité afin
d'assurer la conformité avec les règles métiers. Les tests incluent :
● Test de Création et Mise à jour : Vérification de la création et de la mise à
jour des membres et des médias.
● Tests de Limites : Assurer que les limites d'emprunts sont respectées et que
les membres sont bloqués lorsque cela est nécessaire.
● Tests de Retour des Médias : S'assurer que les états de disponibilité des
médias sont correctement mis à jour lors des retours.

e) Instructions pour Exécuter le Programme

Prérequis:
● Assurez-vous que Python est installé, puis installé Django : pip install django

Cloner le Repository:
Clonez le projet depuis GitHub :
git clone https://github.com/FeuMangue7639/devoir_django

cd mediatheque

Configurer la Base de Données:
Appliquez les migrations pour créer les tables dans la base de données :
python manage.py makemigrations

python manage.py migrate

Démarrer le Serveur:
Lancez le serveur de développement :
python manage.py runserver

Accéder aux Applications:
● Application Bibliothécaire : Accédez à http://127.0.0.1:8000/bibliotheque/.

● Application Membre : Accédez à http://127.0.0.1:8000/emprunteur/.
