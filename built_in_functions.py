import math


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

















