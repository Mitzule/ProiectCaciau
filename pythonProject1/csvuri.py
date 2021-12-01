
import csv
from math import radians, cos, sin, asin, sqrt


def distance(lat1, lat2, lon1, lon2):
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

    c = 2 * asin(sqrt(a))

    r = 6371

    return int(c * r)

def chei():
    cheiTari = []

    with open('country-capitals.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        ok = 0
        for l in csv_reader:
            cheiTari.append(l[0])
    return cheiTari

def timezoneuri():
    timezone={}

    with open( 'country-capitals.csv', 'r') as csv_file:

        csv_reader = csv.reader(csv_file)
        ok=0
        for l in csv_reader:
            timezone[l[0]]=-float(l[2])//15+12
    return timezone



def legaturi():
    leg = {}

    with open('distante.csv', 'r') as csv_file:

        csv_reader = csv.reader(csv_file)
        ok = 0
        for l in csv_reader:
            leg[l[0],l[1]] = l[2]
    return leg


"""
f = open('distante.csv', 'w', newline='')

writer = csv.writer(f)

for i in coordonat:
    for j in coordonat:
        if i!=j:
            writer.writerow([i,j,distance(float(coordonat[i][0]),float(coordonat[j][0]),float(coordonat[i][1]),float(coordonat[j][1]))])
"""