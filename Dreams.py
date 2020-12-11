important = list(input())
dreams = input().split(' -- ')
Max = 0
numbers = []
true_dreams = []
for i in dreams:
    n = list(i)
    for j in n:
        if j in important:
            if j not in numbers:
                Max += 1
                numbers.append(j)
    if Max >= 4:
        true_dreams.append(i)
    numbers = []
    Max = 0
print(' = '.join(true_dreams))