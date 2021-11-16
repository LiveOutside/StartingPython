import csv
from sys import stdin

plants = stdin
with open('plantis.csv', 'w') as file:
    table = csv.writer(file, delimiter=';')
    table.writerow(['nomen', 'definitio', 'pluma', 'Russian nomen',
                    'familia', 'Russian nomen familia'])
    for i in plants:
        if '\n' in i:
            row = i[:-1].split('\t')
            table.writerow([row[j] for j in range(6)])
        else:
            row = i.split('\t')
            table.writerow([row[j] for j in range(6)])
