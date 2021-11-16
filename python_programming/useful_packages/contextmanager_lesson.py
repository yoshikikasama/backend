import contextlib


def tag(name):
    def _tag(f):
        def _wrapper(content):
            print(f'<{name}>')
            r = f(content)
            print(f'/<{name}>')
            return r
        return _wrapper
    return _tag


def f(content):
    print(content)


# tag('h2')(f('test'))
f = tag('h2')(f)
f('test')

