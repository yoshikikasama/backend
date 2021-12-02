import numpy as np
from numpy.core.shape_base import vstack

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(a[0])
print(a[0][0])
# 何x何の配列かを表示
print(a.shape)
# 何次元の配列かを表示
print(a.ndim)
print(a.dtype.name)
print(a.size)
print(np.arange(0, 30, 5))
print(np.arange(0, 2, 0.3))
print(np.ones((3, 4), dtype=np.int16))
print([np.nan] * 10)
print(np.linspace(0, 2, 9))
print(np.arange(24).reshape(2, 3, 4))
x = np.arange(0, 10, 2)
y = np.arange(5)
z = np.arange(0, 100, 20)
print(np.append(x, y))
print(np.vstack([x, y, z]))
print(np.hstack([x, y, z]))
a = np.array([10, 20, 30, 40, 50])
b = np.arange(5)
print(a - b)
print(a < 30)
a = np.ones((2, 3), dtype=int)
# print(a *= 3)
a = np.random.random((2, 3))
print(a.sum())
a = np.arange(12).reshape(3, 4)
print(a)
print(a.sum(axis=0))
print(a.sum(axis=1))
print(a.T)
print(a.resize((2, 6)))