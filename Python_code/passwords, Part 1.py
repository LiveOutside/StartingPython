keyboard = ['qwe', 'wer', 'ert', 'rty', 'tyu', 'yui', 'uio', 'iop',
            'asd', 'sdf', 'dfg', 'fgh', 'ghj', 'hjk', 'jkl',
            'zxc', 'xcv', 'cvb', 'vbn', 'bnm',
            'йцу', 'цук', 'уке', 'кен', 'енг', 'нгш', 'гшщ', 'шщз', 'щзх', 'зхъ',
            'фыв', 'ыва', 'вап', 'апр', 'про', 'рол', 'олд', 'лдж', 'джэ',
            'ячс', 'чсм', 'сми', 'мит', 'ить', 'тьб', 'ьбю', 'жэё'
            ]


class PasswordError(Exception):
    password = input()
    fl1 = False
    fl2 = False
    if len(password) > 8:
        if not(password.islower()) and not(password.isupper()):
            if any([i in password for i in '0123456789']):
                if not(password.isdigit()):
                    if not(any([i in password.lower() for i in keyboard])):
                        print('ok')
                    else:
                        print('error')
                else:
                    print('error')
            else:
                print('error')
        else:
            print('error')
    else:
        print('error')


