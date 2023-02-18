import csv

def handle_uploaded_file(f, f_name="tmp.csv"):
    with open(f_name, 'wb+') as destination:
        for chunk in f.chunks():
            print(chunk)
            destination.write(chunk)
    return f_name

def read_csv(f):
    with open(f) as csvdatei:
        csv_reader_object = csv.DictReader(csvdatei, delimiter=';')
        print(csv_reader_object)
        i = 0
        # for satz in csv_reader_object:
        #     print(i, satz)
        #     i += 1
        # print("Gesammt", i)