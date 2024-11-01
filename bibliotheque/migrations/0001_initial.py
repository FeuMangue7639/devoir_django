# Generated by Django 5.1.2 on 2024-10-30 21:18

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('disponible', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JeuDePlateau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('createur', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('bloque', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CD',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bibliotheque.media')),
                ('artiste', models.CharField(max_length=100)),
            ],
            bases=('bibliotheque.media',),
        ),
        migrations.CreateModel(
            name='DVD',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bibliotheque.media')),
                ('realisateur', models.CharField(max_length=100)),
            ],
            bases=('bibliotheque.media',),
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('media_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='bibliotheque.media')),
                ('auteur', models.CharField(max_length=100)),
            ],
            bases=('bibliotheque.media',),
        ),
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_emprunt', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_retour', models.DateTimeField(default=datetime.datetime(2024, 11, 6, 21, 18, 53, 5955, tzinfo=datetime.timezone.utc))),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliotheque.media')),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliotheque.membre')),
            ],
        ),
    ]
