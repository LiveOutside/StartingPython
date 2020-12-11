successful_circles = 0
successful_experiment = 0
d = int(input())
n = int(input())
s = input()
lam = 0
while s != 'КОНЕЦ ЭКСПЕРИМЕНТА':
    for i in range(1, n + 1):
        if int(s) > 5000:
            print(i, successful_experiment)
            successful_circles += successful_experiment
            successful_experiment = 0
        lam = 12431.25 / int(s)
    number = d / lam
    if abs(number - round(number)) <= 0.1:
        successful_experiment += 1
    s = input()
print('Общее количество успешных экспериментов:', successful_circles)