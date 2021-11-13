def cached(func):
    cache = {}

    def decorated(*args, **kwargs):
        nonlocal cache
        if tuple(args) in cache:
            return cache[tuple(args)]
        else:
            result = func(*args, **kwargs)
            cache[tuple(args)] = result
            return result

    return decorated
