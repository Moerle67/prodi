# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render
import csv

from .forms import *
from .models import *

from .tools import handle_uploaded_file

def form1(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'form1.html', {'form': form})


def upload_file_reha(request):
    print(request.method)
    if request.method == 'POST':
        form = UploadFileForm(request.FILES)
        # print(form.is_valid())
        if True:
            f = request.FILES['file']
            f_name=handle_uploaded_file(f)
            read_csv_reha(f_name)
            return HttpResponseRedirect('/success/url/')
        else:
            print(form.errors)
    else:
        form = UploadFileForm()
    return render(request, 'form1.html', {'form': form})

def read_csv_reha(f):
    # Alle Datensätze löschen
    # Felder CSV
    feld_massnahmentitel = 0
    feld_kategorie = 1
    feld_kategorie_bezeichnung = 2
    feld_abrechnungsart = 3
    feld_dauer = 4
    feld_praxisdauer = 5
    feld_abschluss = 6
    feld_schlagrichtung = 7
    feld_schlagwörter = 8
    feld_kostentraeger = 9
    feld_status = 10
    feld_dokumente = 11
    feld_maßnahmenverantwortlich = 12
    feld_organisation = 13
    feld_orga_ansprechpartner = 14

    Reha.objects.all().delete()
    with open(f, encoding='utf-8') as csvdatei:
        csv_reader_object = csv.reader(csvdatei, delimiter=';')
        print(type(csv_reader_object))
        zeile = 0
        for satz in csv_reader_object:
            zeile += 1
            if zeile == 1:
                continue    # Überschriften
            if len(satz[0].strip()) == 0:
               continue    # Leer Datensätze
            ds = Reha()
            # Maßnamentitel 
            ds.massnahmentitel = satz[feld_massnahmentitel].strip()
            
            # Fachrichtung
            print(f"Fachrichtung {satz[feld_kategorie].strip()}, {satz[feld_kategorie_bezeichnung].strip()} wurde eingelesen.")

            # Fachrichtung            
            fachrichtung, created = Fachrichtung.objects.get_or_create(kategorie=satz[feld_kategorie].strip().strip("\n"))
            if created:
                print(f"Fachrichtung {satz[feld_kategorie].strip()}, {satz[feld_kategorie_bezeichnung].strip()} wurde erstellt.")
            fachrichtung.bezeichnung = satz[feld_kategorie_bezeichnung].strip().strip('\n')
            fachrichtung.save()
            ds.fachrichtung = fachrichtung

            # abrechnungsart
            ds.abrechnungsart = satz[feld_abrechnungsart].strip()

            # Dauer
            ds.dauer = satz[feld_dauer].strip()

            # Praxisdauer 
            ds.praxisdauer = satz[feld_praxisdauer].strip()

            # Abschluss
            ds.abschluss = satz[feld_abschluss].strip()

            # Schlagrichtung
            ds.schlagrichtung = satz[feld_schlagrichtung]


            if satz[feld_status] == "aktiv":
                ds.status = True
            else:
                ds.status = False

            # Dokumente
            dokument_field = Dokument.objects.filter(bezeichnung=satz[feld_dokumente].strip())
            if len(dokument_field) == 0:
                dokument = Dokument()
                dokument.bezeichnung = satz[feld_dokumente]
                dokument.save()
                ds.dokumente = dokument
                print(f"Dokumente {satz[feld_dokumente]} erstellt.")
            else:
                ds.dokumente = dokument_field[0]

            # Maßnahmenverantwortlicher

            mv_name= satz[feld_maßnahmenverantwortlich].strip()
            mv_ds = Kontakt.objects.filter(name=mv_name)
            if len(mv_ds) == 0:
                mv_ds = Kontakt()
                mv_ds.name=satz[feld_maßnahmenverantwortlich]
                mv_ds.save()
                ds.verantwortlicher = mv_ds
            else:
                ds.verantwortlicher = mv_ds[0]
            
            # Organisation

            organisation = satz[feld_organisation].strip()
            print(zeile, organisation)
            organisation_ds = Organisation.objects.filter(bezeichnung=organisation)
            if len(organisation_ds) == 0:
                orga_ds = Organisation()
                orga_ds.bezeichnung = organisation
                kontakt_daten = satz[feld_orga_ansprechpartner].split('\n')
                kt_ds = Kontakt.objects.filter(name=kontakt_daten[0])
                if len(kt_ds) == 0:
                    kt_ds = Kontakt()
                    kt_ds.name=kontakt_daten[0]
                    kt_ds.mail = kontakt_daten[1]
                    kt_ds.telefon = kontakt_daten[2]
                    kt_ds.save()
                    orga_ds.ansprechpartner = kt_ds
                else:
                    orga_ds.ansprechpartner = kt_ds[0]
                orga_ds.save()
                ds.organisation=orga_ds
            else:
                ds.organisation=organisation_ds[0]
            
            # fertig
            ds.save()

            # Schlagwörter
            liste_schlagwörter = satz[feld_schlagwörter].split(',')
            for schlagwort in liste_schlagwörter:
                schlagwort = schlagwort.strip()
                ds_schlagwort, create = Schlagwort.objects.get_or_create(schlagwort=schlagwort)
                ds.schlagwort.add(ds_schlagwort)

            # Kostenträger
            liste_kostentraeger = satz[feld_kostentraeger].split('\n')
            for kostentraeger in liste_kostentraeger:
                kostentraeger = kostentraeger.strip()
                ds_kostentraeger, create = Kostentraeger.objects.get_or_create(kostentraeger=kostentraeger)
                ds.kostentraeger.add(ds_kostentraeger)

        print(f"Es wurden {zeile} Datensätze erfasst.")

def upload_file_fari(request):
    print(request.method)
    if request.method == 'POST':
        form = UploadFileForm(request.FILES)
        # print(form.is_valid())
        if True:
            f = request.FILES['file']
            f_name=handle_uploaded_file(f)
            read_csv_fari(f_name)
            return HttpResponseRedirect('/success/url/')
        else:
            print(form.errors)
    else:
        form = UploadFileForm()
    return render(request, 'form1.html', {'form': form})

def read_csv_fari(f):
    # Alle Datensätze löschen
    Fachrichtung.objects.all().delete()
    with open(f, encoding='utf-8') as csvdatei:
        csv_reader_object = csv.reader(csvdatei, delimiter=';')
        zeile = 0
        for satz in csv_reader_object:
            zeile += 1
            if zeile == 1: #Überschriften
                continue
            if len(satz[0].strip())>0:
                ds = Fachrichtung()
                # Maßnamentitel 
                ds.kategorie = satz[0].strip()
                ds.bezeichnung = satz[1].strip()
                ds.kunde=satz[2].strip()
                ds.save()
            # Fachrichtung
    print(f"Es wurden {zeile} Datensätze erfasst.")
    