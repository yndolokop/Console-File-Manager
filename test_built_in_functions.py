import math

def total(xs: list[float]) -> float:
    result: float = 0.0
    for x in xs:
        result += x
    return result


def join(xs: list[int], delimiter: str) -> int:
    result: str = ''
    for item in xs:
        if result == '':
            result = str(item)
        else:
            result += delimiter + str(item)
    return result


def clean_list(x):
    return list(filter(None, x))


def my_filter(iterable, function):
    return list(filter(function, iterable))


def my_map(iterable, function):
    return list(map(function, iterable))


def my_sorted(iterable, **kwargs):
    return sorted(iterable, **kwargs)


def my_pi():
    return math.pi


def my_pow(*args):
    return pow(*args)


def my_hypot(*args):
    return math.hypot(*args)

















