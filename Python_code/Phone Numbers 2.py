def telephone(tel):
    try:
        tel = ''.join(tel.split())
        if tel.startswith('+7') or tel.startswith('8'):
            if tel.count('(') != tel.count(')') \
                    or tel.count('(') > 1:
                return 'error'
            elif tel[-1] == '-' or tel.count('--') != 0:
                return 'error'
            else:
                if tel.startswith('8'):
                    tel = '+7' + tel[1:]
                res = ''
                for i in tel:
                    if i not in '-()':
                        res += i
                if len(res) == 12:
                    return res
                else:
                    raise ValueError
        else:
            raise ValueError
    except Exception:
        return 'error'


if __name__ == '__main__':
    print(telephone(input()))
