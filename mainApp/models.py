from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Davlat(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = "Davlatlar"


class Pozitsiya(models.Model):
    nom = models.CharField(max_length=255)
    turi = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.nom} {self.turi}"

    class Meta:
        verbose_name_plural = "pozitsiya"
class Club(models.Model):
    nom = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='clublar/')
    prezident = models.CharField(max_length=255, blank=True, null=True)
    trener = models.CharField(max_length=255)
    t_sana = models.DateField(blank=True, null=True)
    kapital = models.PositiveIntegerField(blank=True, null=True)
    davlat = models.ForeignKey(Davlat, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = "Clublar"

class Player(models.Model):
    ism = models.CharField(max_length=255)
    son = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(99)])
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True)
    t_sana = models.DateField(blank=True, null=True)
    maosh = models.PositiveIntegerField(blank=True, null=True)
    narx = models.PositiveIntegerField(blank=True, null=True)
    davlat = models.ForeignKey(Davlat, on_delete=models.SET_NULL, null=True)
    pozitsiya = models.ForeignKey(Pozitsiya, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.ism}"

    class Meta:
        verbose_name_plural = "Playerlar"