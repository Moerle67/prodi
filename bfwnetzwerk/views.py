# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render

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


def upload_file(request):
    print(request.method)
    if request.method == 'POST':
        form = UploadFileForm(request.FILES)
        # print(form.is_valid())
        if True:
            f = request.FILES['file']
            print(f)
            handle_uploaded_file(f)
            return HttpResponseRedirect('/success/url/')
        else:
            print(form.errors)
    else:
        form = UploadFileForm()
    return render(request, 'form1.html', {'form': form})
