from django.db import models
from datetime import date
from django.urls import reverse

OK = {
    'Yes': 'oui',
    'No': 'non',
}
SEX = {
        'M': 'Masculin',
        'F': 'Feminin'
    }
class Province(models.Model):
    code_province = models.BigAutoField(primary_key=True)
    nom_province = models.CharField(max_length=20, null=False)

    def __str__(self) -> str:
        return self.nom_province
    
class ZoneSanitaire(models.Model):
    code_zone = models.BigAutoField(primary_key=True)
    nom_zone = models.CharField(max_length=20, null=False)
    address = models.CharField(max_length=30, null=False)
    code_province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nom_zone

class AireSanitaire(models.Model):
    code_aire = models.BigAutoField(primary_key=True)
    nom_aire = models.CharField(max_length=20, null=False)
    address = models.CharField(max_length=20, null=True)
    code_zone = models.ForeignKey(ZoneSanitaire, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.nom_aire

class Enfant(models.Model):
    code_id = models.BigAutoField(primary_key=True)
    SEX = {
        'M': 'Masculin',
        'F': 'Feminin'
    }
    nom = models.CharField(max_length=25, null=True)
    postnom = models.CharField(max_length=25, null=False)
    prenom = models.CharField(max_length=25, null=True)
    sex = models.CharField(choices=SEX, max_length=10)
    date_naissance = models.DateField(blank=True,null=True)
    jour = models.IntegerField(null=True, blank=True)
    mois = models.IntegerField(null=True, blank=True)
    annee = models.IntegerField(null=True, blank=True)
    age_en_mois = models.IntegerField(null=True, blank=True)
    age_en_annee = models.IntegerField(null=True, blank=True)
    age_en_annee_mois = models.CharField(max_length=30, null=True, blank=True)
    age_en_annee_mois_jour = models.CharField(max_length=30, null=True, blank=True)
    age_inconnu = models.CharField(max_length=20, choices=OK)
    avenue = models.CharField(max_length=20, null=False)
    quartier = models.CharField(max_length=50, null=False)
    commune = models.CharField(max_length=20, null=True)
    ville = models.CharField(max_length=20, null=True)
    code_aire = models.ForeignKey(AireSanitaire, on_delete=models.CASCADE, null=True, blank=True)

    def age_in_years(self):
        today = date.today()
        self.age_en_annee = today.year - self.annee - ((today.month, today.day) < (self.mois, self.jour))
        return self.age_en_annee

    def age_in_months(self):
        today = date.today()
        self.age_en_mois = (today.year - self.annee) * 12 + today.month - self.mois - (
                today.day < self.jour)
        return self.age_en_mois

    def age_in_years_months(self):
        years = self.age_in_years()
        months = self.age_in_months() - years * 12
        self.age_en_annee_mois = f"{years} ans, {months} mois"

    def age_in_years_months_days(self):
        today = date.today()
        birthdate = date(self.annee, self.mois, self.jour)
        age = today - birthdate
        years = age.days // 365
        months = (age.days % 365) // 30
        days = (age.days % 365) % 30
        self.age_en_annee_mois_jour = f"{years} ans, {months} mois, {days} jours"

    def save(self, *args, **kwargs):
        # Extraire le jour, le mois et l'année de my_date_field
        if self.date_naissance:
            self.jour = self.date_naissance.day
            self.mois = self.date_naissance.month
            self.annee = self.date_naissance.year
            self.age_in_years_months()
            self.age_in_years_months_days()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nom
