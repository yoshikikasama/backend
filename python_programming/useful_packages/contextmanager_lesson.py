import contextlib


# def tag(name):
#     def _tag(f):
#         def _wrapper(content):
#             print(f'<{name}>')
#             r = f(content)
#             print(f'/<{name}>')
#             return r
#         return _wrapper
#     return _tag


# def f(content):
#     print(content)


# # tag('h2')(f('test'))
# f = tag('h2')(f)
# f('test')


@contextlib.contextmanager
def tag(name):
    print(f'<{name}>')
    # f(content)がyieldで実行される
    yield
    print(f'/<{name}>')

# @tag('h2')
# def f(content):
#     print(content)

# f('test')


def f():
    print('test0')
    with tag('h2'):
        print('test')
        with tag('h5'):
            print('test2')
f()
