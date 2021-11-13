length = int(input('Введите длину: '))
height = int(input('Введите высоту: '))
col = 0
print(' ', end='')
print('-' * (length + 2))
for row in range(length + 1):
    for col in range(0, height + 2):
        if col == row:
            print('|', ' ' * length, '|', end='\n')
print(' ', end='')
print('-' * (length + 2))
