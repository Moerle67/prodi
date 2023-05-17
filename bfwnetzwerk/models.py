from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Fachrichtung(models.Model):
    kategorie = models.CharField(verbose_name=("Kategorie"), max_length=50, primary_key=True)
    bezeichnung = models.CharField(verbose_name=("Bezeichnung"), max_length=255, blank=True)
    kunde = models.CharField(verbose_name=("Kunde"), max_length=255, blank=True)
    aktiv = models.BooleanField(verbose_name=("Aktiv"), default=True)
    def __str__(self):
        return f"{self.kategorie} - {self.bezeichnung}"
    class Meta:
        verbose_name_plural = "Fachrichtungen"
        verbose_name = "Fachrichtung"
        ordering = ['kategorie']


class Organisation(models.Model):
    bezeichnung = models.CharField(verbose_name=("Organisation"), max_length=255, primary_key=True)
    ansprechpartner = models.CharField(verbose_name="Ansprechpartner", max_length=100)
    ansprechpartner_mail = models.CharField(verbose_name="Ansprechpartner Mail", max_length=50, blank=True)
    ansprechpartner_telefon = models.CharField(verbose_name="Ansprechpartner Telefon", max_length=50, blank=True)
    ansprechpartner2 = models.CharField(verbose_name="Ansprechpartner2", max_length=100, blank=True)
    ansprechpartner2_mail = models.CharField(verbose_name="Ansprechpartner2 Mail", max_length=50, blank=True)
    ansprechpartner2_telefon = models.CharField(verbose_name="Ansprechpartner2 Telefon", max_length=50, blank=True)
    def __str__(self):
        return f"{self.bezeichnung}/{self.ansprechpartner} - {self.ansprechpartner_mail}"
    class Meta:
        verbose_name_plural = "Organisationen"
        verbose_name = "Organisation"

class Schlagwort(models.Model):
    schlagwort = models.CharField(verbose_name=("Schlagwort"), max_length=250, unique=True)
    def __str__(self):
        return f"{self.schlagwort}"
    class Meta:
        verbose_name_plural = "Schlagwort"
        verbose_name = "Schlagworte"
        ordering = ['schlagwort']

class Kostentraeger(models.Model):
    kostentraeger = models.CharField(verbose_name=("Geschäftsfeld/Kostenträger"), max_length=250, unique=True)
    anmerkung = models.CharField(verbose_name=('Anmerkung'), max_length=250, blank=True)
    
    def __str__(self):
        return f"{self.kostentraeger}"
    class Meta:
        verbose_name_plural = "Kostenträger"
        verbose_name = "Kostenträger"
        ordering = ['kostentraeger']

class Reha(models.Model):
    massnahmentitel = models.TextField(verbose_name=("Maßnahmentitel"))
    fachrichtung = models.ManyToManyField(Fachrichtung, verbose_name=("Produkt(e)"), blank = True)
    abrechnungsart = models.CharField(verbose_name=("Abrechnungsart"), max_length=50)
    dauer = models.CharField(verbose_name=("Dauer"), max_length=50)
    praxisdauer = models.CharField(verbose_name=("Praxisdauer"), max_length=50)
    abschluss = models.TextField(verbose_name=("Abschluss"),blank=True)
    schlagrichtung = models.TextField(verbose_name=("inhalt. Schlagrichtung"))
    schlagwort = models.ManyToManyField(Schlagwort, verbose_name=("Schlagwort"))
    kostentraeger = models.ManyToManyField(Kostentraeger, verbose_name=("Geschäftfeld/Kostenträger"))
    status = models.BooleanField(verbose_name=("aktiv"))
    dokumente =   models.URLField(verbose_name="Dokument", max_length=200)
    organisation = models.ForeignKey(Organisation, verbose_name=("Organisation"), on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.massnahmentitel} - {self.organisation}"
    class Meta:
        verbose_name_plural = "Produkte"
        verbose_name = "Produkt"
 
class Vorschlag(models.Model):
    vorschlag = models.CharField(verbose_name=("Vorschlag"), max_length=50)
    begruendung = models.TextField(verbose_name=("Begründung"))
    vorschlagdatum = models.DateField(verbose_name=("vorgeschlagen am"), auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, verbose_name=("Benutzer"), editable=False,null=True,blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.vorschlag}/{self.user} ({self.vorschlagdatum})"
    class Meta:
        verbose_name_plural = "Vorschläge"
        verbose_name = "Vorschlag"

class Vorschlagbearbeitung(models.Model):
    vorschlag = models.ForeignKey(Vorschlag, verbose_name=("Vorschlag"), on_delete=models.CASCADE)
    anmerkung = models.TextField(verbose_name=("Anmerkung"))
    erledigt = models.BooleanField(verbose_name=("Erledigt"), default=False)
    datum = models.DateField(verbose_name=("Datum"), auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, verbose_name=("Benutzer"), editable=False, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.vorschlag.vorschlag} - {self.anmerkung} - {self.user}/ {self.erledigt}"
    class Meta:
        verbose_name_plural = "V.Bearbeitungen"
        verbose_name = "V.Bearbeitung"

