import contextlib


def tag(f):
    def _wrapper(content):
        print('<h2>')
        r = f(content)
        print('</h2>')
        return r
    return _wrapper


# @tag
def f(content):
    print(content)


f = tag(f('test'))
# f('test')
