s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')
print(is_start)

print('#'*10)
print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())

print('My name is {name} {family}. Watashiha {family} {name}です。'.format(
    name='yoshiki', family='Kasama'))

X = 20
Y = X
Y = 5
print(id(X))
print(id(Y))
print(X)
print(Y)

x = ['a', 'b']
y = x
y[0] = 'p'
print(id(x))
print(id(y))
print(x)
print(y)

min, max = 0, 100
print(min, max)

# tappleは中身を書き換えない変数に使用する

x = (1+2 +
     3+4+4)

print(x)

for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)

days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)


y = 'None'
x = 1 if y else 2
print(x)
