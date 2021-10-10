def other_func(f):
    print(f(10))


def test_func(x):
    return x * 2


def test_func2(x):
    return x * 5


other_func(test_func)
other_func(test_func2)
other_func(lambda x: x * 2)
other_func(lambda x: x * 5)
