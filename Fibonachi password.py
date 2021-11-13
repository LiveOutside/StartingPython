def check_password(func):
    count = 0
    password = 'пидарас'
    passinput = ''

    def decorated(*args, **kwargs):
        nonlocal password, passinput, count
        if passinput != password:
            passinput = input('Введите пароль: ').strip()
            if passinput != password:
                print('В доступе отказано!')
                return None
        count += 1
        res = func(*args, **kwargs)
        count -= 1
        if count == 0:
            passinput = ''
        return res
    return decorated

check_password("пидарас")