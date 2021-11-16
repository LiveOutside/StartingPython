pirate1 = input()
pirate2 = input()
if pirate1 == pirate2:
    print('ничья')
if pirate1 == 'ножницы' and pirate2 == 'бумага':
    print('первый')
if pirate1 == 'бумага' and pirate2 == 'ножницы':
    print('второй')
if pirate1 == 'камень' and pirate2 == 'ножницы':
    print('первый')
if pirate1 == 'ножницы' and pirate2 == 'камень':
    print('второй')
if pirate1 == 'камень' and pirate2 == 'бумага':
    print('первый')
if pirate1 == 'бумага' and pirate2 == 'камень':
    print('второй')
