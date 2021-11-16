class NotEnoughError(Exception):
    pass


def stubbornness(*data):
    result = []
    for i in data:
        if max(i) == 0 or min(i) == 0:
            raise ZeroDivisionError('Cannot be divided by zero')
        if 0 < len(i) < 2:
            raise NotEnoughError('Not enough values')
        result.append(calc(i)) if calc(i) else None
    if not result:
        raise IndexError('Empty Return Error')
    else:
        return sorted(result)


def calc(i):
    if i[0] % max(i) == 0 and i[0] % min(i) == 0:
        return i[0]


data = [(8, 2, 16),
        (14, 6, 1, 7, 14),
        (6, 9), (8, 1, 8)]
print(*stubbornness(*data))
