import csv
from .models import CodigoPostal

def leer_cvs():
    with open('polls/cp_filtrada.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            zip = CodigoPostal(codigo=row['d_codigo'], municipio=row['d_asenta-D_mnpio'])
            zip.save()
