import functools


def d(f):
    @functools.wraps(f)
    def w():
        """ Wrapper docstring"""
        print('decorator')
        return f()
    return w


@d
def example():
    """example docstring"""
    print('example')


example()
print(example.__doc__)
