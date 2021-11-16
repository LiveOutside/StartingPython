act = input().split(' -> ')
n = int(input())
for i in range(n):
    acts = input()
    for j in range(len(act)):
        if acts == act[j]:
            if j - 1 < 0:
                print(f'{acts} -> {act[j + 1]}')
            elif j + 1 == len(act):
                print(f'{act[j - 1]} -> {acts}')
            else:
                print(f'{act[j - 1]}  -> {acts} -> {act[j + 1]}')
