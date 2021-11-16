class NotEnoughError(Exception):
    pass


def check(cort):
    if cort[0] % max(cort) == 0 and cort[0] % min(cort) == 0:
        return cort[0]


def stubbornness(*data):
    res = []
    for cort in data:
        if max(cort) == 0 or min(cort) == 0:
            raise ZeroDivisionError('Cannot be divided by zero.')
        if 0 < len(cort) < 2:
            raise NotEnoughError('Not enough values.')
        res.append(check(cort)) if check(cort) else None
    if not res:
        raise IndexError('Empty Return Error')
    else:
        return sorted(res)


data = [(8, 2, 16),
        (14, 6, 1, 7, 14),
        (6, 9), (8, 1, 8)]
print(*stubbornness(*data))
