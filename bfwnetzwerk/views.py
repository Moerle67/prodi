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


def upload_file_prod(request):
    if request.method == 'POST':
        form = UploadFileForm(request.FILES)
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
    feld_massnahmeart = 1
    feld_schlagrichtung = 2
    feld_schlagwort = 3
    feld_abrechnungsart = 4
    feld_kostentraeger = 5
    feld_dauer = 6
    feld_praxisdauer = 7
    feld_abschluss = 8
    feld_status = 9
    feld_dokument = 10
    feld_organisation = 11
    feld_ansprechpartner = 12
    feld_ansprechpartner2 = 13
    

    Produkt.objects.all().delete()
    with open(f, encoding='utf-8') as csvdatei:
        csv_reader_object = csv.reader(csvdatei, delimiter=';')
        zeile = 0
        for satz in csv_reader_object:
            zeile += 1
            if zeile == 1:
                continue    # Überschriften
            if len(satz[0].strip()) == 0:
               continue    # Leer Datensätze
            ds = Produkt()
            
            # Maßnamentitel 
            ds.massnahmentitel = satz[feld_massnahmentitel].strip()[:240]
            
            # Massnahmeart
            massnahmeart = satz[feld_massnahmeart].strip()[:240]
            ds_massnahmeart = Massnahmeart.objects.filter(art=massnahmeart)
            if len(ds_massnahmeart) == 0:
                # Noch nicht vorhaneden
                ds_massnahmeart = Massnahmeart()
                ds_massnahmeart.art = massnahmeart # type: ignore
                ds_massnahmeart.save()
                ds.massnahmeart = ds_massnahmeart
            else:
                # Vorhanden zuordnung des ersten Treffers
                ds.massnahmeart = ds_massnahmeart[0]

            # Schlagrichtung 
            ds.schlagrichtung = satz[feld_schlagrichtung].strip()
   
            # Schlagwörter
            # Many to many

            # Abrechnungsart
            # Many to many

            # Kostenträger 
            # Many to many
            
            # Dauer
            ds.dauer = satz[feld_dauer].strip()[:140]
            
            # Praxisdauer
            ds.praxisdauer = satz[feld_praxisdauer].strip()[:140]

            # Abschluss
            # Many to many

            # Status
            if satz[feld_status] == "aktiv":
                ds.status = True
            else:
                ds.status = False

            # Dokument
            ds.dokument = satz[feld_dokument].strip() # type: ignore
            
            # Organisation
            organisation = satz[feld_organisation].strip()
            ds_organisation = Organisation.objects.filter(bezeichnung=organisation)
            if len(ds_organisation) == 0:
                # Noch nicht vorhanden
                ds_organisation = Organisation()
                ds_organisation.bezeichnung = organisation
                ap = satz[feld_ansprechpartner].split('\n')
                if len(ap)>1:
                    ds_organisation.ansprechpartner = ap[0]
                    ds_organisation.ansprechpartner_mail = ap[1]
                    ds_organisation.ansprechpartner_telefon = ap[2] 

                ap = satz[feld_ansprechpartner2].split('\n')
                if len(ap)>1:
                    ds_organisation.ansprechpartner2 = ap[0]
                    ds_organisation.ansprechpartner2_mail = ap[1]
                    ds_organisation.ansprechpartner2_telefon = ap[2] 
                ds_organisation.save()
                ds.organisation = ds_organisation
            else:
                # Vorhanden zuordnung des ersten Treffers
                ds.organisation = ds_organisation[0]
            ds.save()

            # Many to Many

            # Schlagwörter
            liste_schlagwoerter = satz[feld_schlagwort].split(',')
            for schlagwort in liste_schlagwoerter:
                schlagwort = schlagwort.strip()[:240]
                ds_schlagwort, create = Schlagwort.objects.get_or_create(schlagwort=schlagwort)
                ds.schlagwoerter.add(ds_schlagwort)
            del liste_schlagwoerter  
            
            # Abrechnungsart
            liste_abrechnungsart = satz[feld_abrechnungsart].split(',')
            for abrechnungsart in liste_abrechnungsart:
                abrechnungsart = abrechnungsart.strip()[:240]
                ds_abrechnungsart, create = Abrechnungsart.objects.get_or_create(kunde=abrechnungsart)
                ds.abrechnungsart.add(ds_abrechnungsart)
            del liste_abrechnungsart

            # Kostenträger
            liste_kt = satz[feld_kostentraeger].split('\n')
            for kt in liste_kt:
                kt = kt.strip()[:240]
                ds_kt, create = Kostentraeger.objects.get_or_create(kostentraeger=kt)
                ds.kostentraeger.add(ds_kt)
            del liste_kt

            # Abschluss
            liste_abschluss = satz[feld_abschluss].split('\n')
            for abschluss in liste_abschluss:
                abschluss = abschluss.strip()[:240]
                ds_abschluss, create = Abschluss.objects.get_or_create(name=abschluss)
                ds.abschluss.add(ds_abschluss)
            del liste_abschluss

        print(f"Es wurden {zeile} Datensätze erfasst.")
