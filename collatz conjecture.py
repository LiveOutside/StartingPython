Num = int(input('Начальное число: '))
O = 0
N = 0
Case = list()
Case.append(Num)
Case.append(Num)
for Num in range(10958):
    Case.append(Case[N] + Case[N + 1])
    N += 1
while Case[-1] != 1:
    if Case[-1] % 2 == 0:
        Case[-1] = Case[-1] // 2
    else:
        Case[-1] = Case[-1] * 3 + 1
    #print(Case[-1], end='\n')
    print(Case)