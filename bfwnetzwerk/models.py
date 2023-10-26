from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Massnahmeart(models.Model):
    art = models.CharField(verbose_name=("Kategorie"), max_length=250, primary_key=True)
    bezeichnung = models.CharField(verbose_name=("Bezeichnung"), max_length=255, blank=True, null=True)
    def __str__(self):
        return f"{self.art}"
    class Meta:
        verbose_name_plural = "Maßnahmearten"
        verbose_name = "Maßnahmeart"
        ordering = ['art']


class Organisation(models.Model):
    bezeichnung = models.CharField(verbose_name=("Organisation"), max_length=255, primary_key=True)
    ansprechpartner = models.CharField(verbose_name="Ansprechpartner", max_length=100)
    ansprechpartner_mail = models.CharField(verbose_name="Ansprechpartner Mail", max_length=50, blank=True, null=True)
    ansprechpartner_telefon = models.CharField(verbose_name="Ansprechpartner Telefon", max_length=50, blank=True, null=True)
    ansprechpartner2 = models.CharField(verbose_name="Ansprechpartner2", max_length=100, blank=True, null=True)
    ansprechpartner2_mail = models.CharField(verbose_name="Ansprechpartner2 Mail", max_length=50, blank=True, null=True)
    ansprechpartner2_telefon = models.CharField(verbose_name="Ansprechpartner2 Telefon", max_length=50, blank=True, null=True)
    def __str__(self):
        return f"{self.bezeichnung}/{self.ansprechpartner} - {self.ansprechpartner_mail}"
    class Meta:
        verbose_name_plural = "Organisationen"
        verbose_name = "Organisation"
        ordering = ['bezeichnung']

class Schlagwort(models.Model):
    schlagwort = models.CharField(verbose_name=("Schlagwort"), max_length=250, unique=True)
    def __str__(self):
        return f"{self.schlagwort}"
    class Meta:
        verbose_name_plural = "Schlagwort"
        verbose_name = "Schlagworte"
        ordering = ['schlagwort']

class Abrechnungsart(models.Model):
    kunde = models.CharField(verbose_name=("Geschäftsfeld/Kostenträger"), max_length=250, unique=True)
    anmerkung = models.CharField(verbose_name=('Anmerkung'), max_length=250, blank=True, null=True)
    
    def __str__(self):
        return f"{self.kunde}"
    class Meta:
        verbose_name_plural = "Produkte / Abrechnungsart"
        verbose_name = "Produkt / Abrechnungsart"
        ordering = ['kunde']

class Kostentraeger(models.Model):
    kostentraeger = models.CharField(verbose_name="Kostenträger", max_length=250)
    anmerkung = models.TextField(verbose_name="Anmerkung", blank=True, null=True)

    class Meta:
        verbose_name = "Kostenträger"
        verbose_name_plural = "Kostenträger"

    def __str__(self):
        return self.kostentraeger

    def get_absolute_url(self):
        return reverse("kostentraeger_detail", kwargs={"pk": self.pk})

class Abschluss(models.Model):
    name = models.CharField(verbose_name="Abschluss", max_length=250)
    bemerkung = models.TextField(verbose_name="Bemerkung", blank=True, null=True)
    class Meta:
        verbose_name = "Abschluss"
        verbose_name_plural = "Abschlüsse"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Abschluss_detail", kwargs={"pk": self.pk})

class Produkt(models.Model):
    massnahmentitel = models.TextField(verbose_name=("Maßnahmentitel"))
    massnahmeart = models.ManyToManyField(Massnahmeart, verbose_name="Maßnahmenart")
    schlagrichtung = models.TextField(verbose_name="Inhaltliche Schlagrichtung")
    schlagwoerter = models.ManyToManyField(Schlagwort, verbose_name="Schlagwörter")
    abrechnungsart = models.ManyToManyField(Abrechnungsart, verbose_name="Produkt / Abrechnungsart")
    kostentraeger = models.ManyToManyField(Kostentraeger, verbose_name="Kostenträger")
    dauer = models.CharField(verbose_name="Dauer", max_length=150)
    praxisdauer = models.CharField(verbose_name="Praxisdauer", max_length=150, blank=True, null=True)
    abschluss = models.ManyToManyField(Abschluss, verbose_name="Abschluß / Zertifikat")
    status = models.BooleanField(verbose_name="Status", default=True)
    dokument = models.URLField(verbose_name="Dokument", max_length=200, blank=True, null=True)
    organisation = models.ForeignKey(Organisation, verbose_name="Organisation", on_delete=models.RESTRICT)
    def __str__(self):
        return f"{self.massnahmentitel}"
    class Meta:
        verbose_name_plural = "Produkte"
        verbose_name = "Produkt"
        ordering = ["massnahmentitel"]


