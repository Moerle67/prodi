import csv

def handle_uploaded_file(f, f_name="/tmp/tmp.csv"):
    with open(f_name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return f_name

