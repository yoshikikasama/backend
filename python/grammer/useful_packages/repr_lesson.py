# repr representation 表示
# python objectとして表示される
# print('s')
# print(str('s'))
# print(repr('s'))


# import datetime

# d = datetime.datetime.now()

# print(d)
# print(str(d))
# print(repr(d))
# print('{!r} {} {!s}'.format('test1', 'test2', 'test3'))

class Point():
    def __repr__(self) -> str:
        return 'POINT <object>'

    def __str__(self) -> str:
        return 'Point ###'


p = Point()
print('{0!r}'.format(p))
print('{0}'.format(p))
print('{0!s}'.format(p))
