Color = input()
with open('test_n2_res/boat_suits.txt') as file:
    suits = [i for i in file.readlines() if i.split()[1] == Color]

people = len(suits)
name = max([i.split()[0] for i in suits], key=lambda x: (len(x), x))
length = sum([int(i.split()[-1]) for i in suits])

with open('colored_dress.txt', 'w') as file2:
    file2.writelines('\n'.join([str(people), name, str(length)]))
