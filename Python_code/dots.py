col = int(input())
box_dots = []
first = 0
second = 0
third = 0
fourth = 0
for i in range(col):
    dots = input().split()
    if int(dots[0]) == 0 and int(dots[1] != 0):
        print(f'({", ".join(dots)})')
    elif int(dots[1]) == 0 and int(dots[0]) != 0:
        print(f'({", ".join(dots)})')
    elif int(dots[0]) == 0 and int(dots[0]) == 0:
        print(f'({", ".join(dots)})')
    if int(dots[0]) > 0 and int(dots[1]) > 0:
        first += 1
    if int(dots[0]) > 0 and int(dots[1]) < 0:
        fourth += 1
    if int(dots[0]) < 0 and int(dots[1]) > 0:
        second += 1
    if int(dots[0]) < 0 and int(dots[1]) < 0:
        third += 1
print(f'I: {first}, II: {second}, III: {third}, IV: {fourth}.')