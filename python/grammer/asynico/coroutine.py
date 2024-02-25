def g_hello():
    while True:
        r = yield 'hello'
        yield r

# for w in g_hello():
#     print(w)
g = g_hello()
print(next(g))
print(g.send('mike'))
print(next(g))
print(g.send('nancy'))
