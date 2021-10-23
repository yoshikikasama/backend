def say_something():
    print('hi')


print(type(say_something))
f = say_something
f()


# tappleの形で値が入る
def say_something2(*args):
    print(args)
    for arg in args:
        print(arg)


say_something2('Hi', 'Mike', 'Nance')


# key word argsの略称 (辞書の形で値が入る)
def menu(**kwargs):
    print(kwargs)


# menu(entree='beef', drink='coffee')

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}

menu(**d)


def circle_are_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area


ca1 = circle_are_func(3.14)
ca2 = circle_are_func(3.141592)

print(ca1(10))
print(ca2(10))


# 前後に処理を実行できる
def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper


@print_info
def add_num(a, b):
    return a + b


r = add_num(10, 20)
print(r)

l = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']


def change_words(words, func):
    for word in words:
        print(func(word))


# def sample_func(word):
#     return word.capitalize()
# change_words(l, sample_func)
# lambdaでsample_funcを実現可能
# functionを引数とする関数に使用される
change_words(l, lambda word: word.capitalize())


# pythonはyieldをみたらgeneratorとして判断する
def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'
    print('local:', locals())


g = greeting()
print(g)
print(next(g))
print('tes1')
print(next(g))
print('tes2')
print(next(g))

t=(1, 2, 3, 4, 5)

r=[i for i in t if i % 2 == 0]
print(r)

print('global:', globals())
