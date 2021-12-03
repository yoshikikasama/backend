import functools


def f(x, y):
    return x + y


def task(f):
    print('start')
    print(f())

# def outer(x, y):
#     def inner():
#         return x + y
#     return inner


# f = outer(10, 20)
# partialはouter関数と同じ動きをする
p = functools.partial(f, 10, 20)
task(p)
