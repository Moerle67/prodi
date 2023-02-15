from django.db import models

# Create your models here.
class Fachrichtung(models.Model):
    kategorie = models.CharField(verbose_name=("Kategorie"), max_length=50, primary_key=True)
    bezeichnung = models.CharField(verbose_name=("Bezeichnung"), max_length=255)
    kunde = models.CharField(verbose_name=("Kunde"), max_length=255)
    aktiv = models.BooleanField(verbose_name=("Aktiv"))
    def __str__(self):
        return f"{self.kategorie} - {self.bezeichnung}"
    class Meta:
        verbose_name_plural = "Fachrichtungen"

class Kontakt(models.Model):
    name = models.CharField(verbose_name=("Name"), max_length=250)
    mail = models.CharField(verbose_name=("E-Mail"), max_length=250, blank=True)
    telefon = models.CharField(verbose_name=("Telefon"), max_length=50, blank=True)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name_plural = "Kontakte"

class Dokument(models.Model):
    bezeichnung = models.CharField(verbose_name=("Bezeichnung"), max_length=250)
    def __str__(self):
        return f"{self.bezeichnung}"
    class Meta:
        verbose_name_plural = "Dokumente"

class Organisation(models.Model):
    bezeichnung = models.CharField(verbose_name=("Organisation"), max_length=255)
    ansprechpartner = models.ForeignKey(Kontakt, verbose_name=("Ansprechpartner"), on_delete=models.CASCADE)
    def __str__(self):
        return self.bezeichnung
    class Meta:
        verbose_name_plural = "Organisationen"

class Reha(models.Model):
    massnahmentitel = models.CharField(verbose_name=("Maßnahmentitel"), max_length=255)
    fachrichtung = models.ForeignKey(Fachrichtung, verbose_name=("Fachrrichtung"), on_delete=models.CASCADE)
    schlagrichtung = models.TextField(verbose_name=("inhalt. Schlagrichtung"))
    status = models.BooleanField(verbose_name=("Status"))
    verantwortlicher = models.ForeignKey(Kontakt, verbose_name=("Maßnahmenverantwortlicher"), on_delete=models.CASCADE)
    organisation = models.ForeignKey(Organisation, verbose_name=("Organisation"), on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.massnahmentitel} - {self.organisation}"
    class Meta:
        verbose_name_plural = "Rehas"