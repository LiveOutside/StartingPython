def check_password(password):
    def real_password(func):
        def wrapper(*args, **kwargs):
            if password == input('Введите пароль: ').strip():
                return func(*args, **kwargs)
            else:
                print('В доступе отказано')

        return wrapper
    return real_password
