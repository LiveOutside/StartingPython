import csv

percentage = int(input())
with open('vps.csv') as file:
    students = csv.reader(file, delimiter=';')
    students = [i for i in students]
    for specializations in students[1:]:
        if int(specializations[-2]) >= percentage:
            print(specializations[0])
