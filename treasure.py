import sys
coX  = int()
coY = 0
side = 'Север'
print('Укажите напрваление движения: ')
ans = input()
if ans == 'стоп':
    sys.exit()
print('Введите расстояние: ')
move = int(input())
while ans != 'стоп':
    if side == 'Север':
        if ans == 'вперед':
            coY += move
        elif ans == 'разворот':
            side = 'Юг'
        elif ans == 'влево':
            side = 'Запад'
            coX += move
        elif ans == 'вправо':
            side = 'Восток'
            coX -= move
    elif side == 'Юг':
        if ans == 'вперед':
            coY -= move
        elif ans == 'разворот':
            side = 'Север'
        elif ans == 'влево':
            side = 'Восток'
            coX -= move
        elif ans == 'вправо':
            side = 'Запад'
            coX += move
    elif side == 'Восток':
        if ans == 'вперед':
            coX -= move
        elif ans == 'разворот':
            side = 'Запад'
        elif ans == 'влево':
            side = 'Юг'
            coY -= move
        elif ans == 'вправо':
            side = 'Север'
            coY += move
    elif side == 'Запад':
        if ans == 'вперед':
            coX += move
        elif ans == 'разворот':
            side = 'Восток'
        elif ans == 'влево':
            side = 'Север'
            coY += move
        elif ans == 'вправо':
            side = 'Юг'
            coY -= move
    print('Укажите напрваление движения: ')
    ans = input()
    print('Введите расстояние: ')
    move = int(input())
if coY < 0:
    print('Координаты по Y: Юг', abs(coY))
elif coY > 0:
    print('Координаты по Y: Север', coY)
if coX < 0:
    print('Координаты по X: Восток', abs(coX))
elif coX > 0:
    print('Координаты по X: Запад', coX)
    
    