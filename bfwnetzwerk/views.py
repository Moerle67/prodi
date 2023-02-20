# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render
import csv

from .forms import *
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
    Reha.objects.all().delete()
    with open(f) as csvdatei:
        csv_reader_object = csv.reader(csvdatei, delimiter=';')
        print(type(csv_reader_object))
        zeile = 0
        for satz in csv_reader_object:
            zeile += 1
            ds = Reha()
            # Maßnamentitel 
            ds.massnahmentitel = satz[0].strip()
            # Fachrichtung
            fachrichtung = Fachrichtung.objects.get(kategorie=satz[1])
            #if fachrichtung:
                #print(fachrichtung.id)

            # ds.save()

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
    with open(f) as csvdatei:
        csv_reader_object = csv.reader(csvdatei, delimiter=';')
        zeile = 0
        for satz in csv_reader_object:
            zeile += 1
            if zeile == 1: #Überschriften
                continue
            ds = Fachrichtung()
            # Maßnamentitel 
            ds.kategorie = satz[0].strip()
            ds.bezeichnung = satz[1].strip()
            ds.kunde=satz[2].strip()
            ds.save()
            # Fachrichtung
    print(f"Es wurden {zeile} Datensätze erfasst.")
    