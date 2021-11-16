import csv
money = 1000
with open('wares.csv', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    rows = [(i[0], int(i[1])) for i in reader]
rows.sort(key=lambda x: x[1])
if rows[0][1] > money:
    print('error')
res = []
while rows and money >= rows[0][1]:
    count = money // rows[0][1]
    if count > 10:
        count = 10
    money -= count * rows[0][1]
    for i in range(count):
        res.append(rows[0][0])
    rows.pop(0)
print(', '.join(res))
