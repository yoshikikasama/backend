import threading

t1 = threading.local()

print(t1)

t1.val = 10
print(vars(t1))
t1.val1 = 20
print(vars(t1))

# setattr(オブジェクト, 追加したい属性, 値)
# obejctに属性を追加したいときに使われる関数
setattr(t1, 'user', 'test')

print(vars(t1))
