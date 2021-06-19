import csv
f=open('Flowers.csv', 'r')
csvDict= csv.DictReader(f)
for r in csvDict:
    print(dict(r))