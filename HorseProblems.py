flag = False
new_box = []
horse_g = float(input())
horse_b1 = float(input())
horse_b2 = float(input())
night_length = int(input())
destroyed_tens = float(input())
box = [horse_g, horse_b1, horse_b2]
for i in box:
    ooo = i * night_length
    if ooo >= destroyed_tens:
        if i == horse_g:
            new_box.append('Конек-Горбунок')
        elif i == horse_b1:
            new_box.append('Лошадиный брат - 1')
        elif i == horse_b2:
            new_box.append('Лошадиный брат - 2')
print(' '.join(new_box))
if not bool(new_box):
    print('Не они!')
