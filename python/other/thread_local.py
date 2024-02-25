import threading

t1 = threading.local()

print(t1)

t1.val = 10
print(vars(t1))
t1.val1 = 20
print(vars(t1))


setattr(t1, 'user', 'test')

print(vars(t1))
