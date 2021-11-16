tel = ''.join(input().split())
if tel.startswith('+7') or tel.startswith('8'):
    if tel.count('(') != tel.count(')') \
            or tel.count('(') > 1:
        print('error')
    elif tel[-1] == '-' or tel.count('--') != 0:
        print('error')
    else:
        if tel.startswith('8'):
            tel = '+7' + tel[1:]
        res = ''
        for i in tel:
            if i not in '-()':
                res += i
        if len(res) == 12:
            print(res)
        else:
            print('error')
else:
    print('error')
