color = input()
with open('boat_suits.txt') as file:
    boat_suits = [person for person in file.readlines()
                  if person.split()[1] == color]
people = len(boat_suits)
personName = max([i.split()[0] for i in boat_suits], key=lambda x: (len(x), x))
suits = sum([int(i.split()[2]) for i in boat_suits])
with open('colored_dress.txt', 'w') as file2:
    file2.writelines('\n'.join([str(people), personName, str(suits)]))
