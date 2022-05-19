from built_in_functions import my_filter, my_map, my_sorted, my_pi, my_pow, my_hypot


def test_my_filter():
    assert my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5]


def test_my_map():
    assert my_map([1, 2, 3, 4, 5], lambda x: x ** x) == [1, 4, 27, 256, 3125]
    assert my_map([1, 2, 3, 4, 5], lambda x: x ** 0) == [1, 1, 1, 1, 1]
    assert my_map([], lambda x: x ** 1) == []


def test_my_sorted():
    assert my_sorted(['e', 'a', 'u', 'o', 'i']) == ['a', 'e', 'i', 'o', 'u']
    assert my_sorted('Python') == ['P', 'h', 'n', 'o', 't', 'y']
    assert my_sorted(('e', 'a', 'u', 'o', 'i')) == ['a', 'e', 'i', 'o', 'u']
    assert my_sorted([0]) == [0]
    assert my_sorted([(2, 2), (3, 4), (4, 1), (1, 3)], key=lambda x: x[1]) == [(4, 1), (2, 2), (1, 3), (3, 4)]


def test_my_pi():
    assert my_pi() == 3.141592653589793


def test_my_pow():
    assert my_pow(2, 3, 5) == 3


def test_my_hypot():
    assert my_hypot(10, 5) == 11.180339887498949

















