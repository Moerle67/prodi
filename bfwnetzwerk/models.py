from django.db import models
from django.urls import reverse

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

class Kontakt(models.Model):
    name = models.CharField(verbose_name=("Name"), max_length=250, primary_key=True)
    mail = models.CharField(verbose_name=("E-Mail"), max_length=250, blank=True)
    telefon = models.CharField(verbose_name=("Telefon"), max_length=50, blank=True)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name_plural = "Kontakte"
        verbose_name = "Kontakt"

class Dokument(models.Model):
    bezeichnung = models.CharField(verbose_name=("Bezeichnung"), max_length=250)
    def __str__(self):
        return f"{self.bezeichnung}"
    class Meta:
        verbose_name_plural = "Dokumente"
        verbose_name = "Dokument"

class Organisation(models.Model):
    bezeichnung = models.CharField(verbose_name=("Organisation"), max_length=255, primary_key=True)
    ansprechpartner = models.ForeignKey(Kontakt, verbose_name=("Ansprechpartner"), on_delete=models.CASCADE)
    def __str__(self):
        return self.bezeichnung
    class Meta:
        verbose_name_plural = "Organisationen"
        verbose_name = "Organisation"

class Schlagwort(models.Model):
    schlagwort = models.CharField(verbose_name=("Schlagwort"), max_length=50, unique=True)
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
    fachrichtung = models.ForeignKey(Fachrichtung, verbose_name=("Fachrrichtung"), on_delete=models.CASCADE)
    abrechnungsart = models.CharField(verbose_name=("Abrechnungsart"), max_length=50)
    dauer = models.CharField(verbose_name=("Dauer"), max_length=50)
    praxisdauer = models.CharField(verbose_name=("Praxisdauer"), max_length=50)
    abschluss = models.TextField(verbose_name=("Abschluss"),blank=True)
    schlagrichtung = models.TextField(verbose_name=("inhalt. Schlagrichtung"))
    schlagwort = models.ManyToManyField(Schlagwort, verbose_name=("Schlagwort"))
    kostentraeger = models.ManyToManyField(Kostentraeger, verbose_name=("Geschäftfeld/Kostenträger"))
    status = models.BooleanField(verbose_name=("aktiv"))
    dokumente = models.ForeignKey(Dokument, verbose_name=("Dokumente"), on_delete=models.CASCADE)
    verantwortlicher = models.ForeignKey(Kontakt, verbose_name=("Maßnahmenverantwortlicher"), on_delete=models.CASCADE)
    organisation = models.ForeignKey(Organisation, verbose_name=("Organisation"), on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.massnahmentitel} - {self.organisation}"
    class Meta:
        verbose_name_plural = "Rehas"
        verbose_name = "Reha"


