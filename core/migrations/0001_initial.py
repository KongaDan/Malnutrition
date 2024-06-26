# Generated by Django 5.0.2 on 2024-05-01 22:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AireSanitaire',
            fields=[
                ('code_aire', models.BigAutoField(primary_key=True, serialize=False)),
                ('nom_aire', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('code_province', models.BigAutoField(primary_key=True, serialize=False)),
                ('nom_province', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Enfant',
            fields=[
                ('code_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=25, null=True)),
                ('postnom', models.CharField(max_length=25)),
                ('prenom', models.CharField(max_length=25, null=True)),
                ('sex', models.CharField(choices=[('M', 'Masculin'), ('F', 'Feminin')], max_length=10)),
                ('date_naissance', models.DateField()),
                ('jour', models.IntegerField(blank=True, null=True)),
                ('mois', models.IntegerField(blank=True, null=True)),
                ('annee', models.IntegerField(blank=True, null=True)),
                ('age_en_mois', models.IntegerField(blank=True, null=True)),
                ('age_en_annee', models.IntegerField(blank=True, null=True)),
                ('age_en_annee_mois', models.CharField(blank=True, max_length=30, null=True)),
                ('age_en_annee_mois_jour', models.CharField(blank=True, max_length=30, null=True)),
                ('age_inconnu', models.CharField(choices=[('Yes', 'oui'), ('No', 'non')], max_length=20)),
                ('avenue', models.CharField(max_length=20)),
                ('quartier', models.CharField(max_length=50)),
                ('commune', models.CharField(max_length=20, null=True)),
                ('ville', models.CharField(max_length=20, null=True)),
                ('code_aire', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.airesanitaire')),
            ],
        ),
        migrations.CreateModel(
            name='ZoneSanitaire',
            fields=[
                ('code_zone', models.BigAutoField(primary_key=True, serialize=False)),
                ('nom_zone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=30)),
                ('code_province', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='zoneSanitaire', to='core.province')),
            ],
        ),
        migrations.AddField(
            model_name='airesanitaire',
            name='code_zone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.zonesanitaire'),
        ),
    ]
