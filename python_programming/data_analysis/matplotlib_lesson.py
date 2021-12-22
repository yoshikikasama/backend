import matplotlib.pyplot as plt
import numpy as np

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# plt.ylabel('some numbers')
# plt.axis([0, 10, 0, 10])
# plt.show()

# t = np.arange(0, 5, 0.2)
# print(t)
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()

# x = np.random.rand(50)
# y = np.random.rand(50)
# colors = np.random.rand(50)
# area = np.random.rand(50) * 100
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)
# plt.show()

# objects = ('a', 'b', 'c', 'd', 'e', 'f')
# y_pos = np.arange(len(objects))
# value = [1, 2, 3, 4, 5, 6]
# plt.bar(y_pos, value, alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.ylabel('Usage')
# plt.title('Title')
# plt.show()

# labels = ('Python', 'java', 'C++', 'Ruby')
# sizes = [10, 20, 30, 40]
# colors = ['red', 'green', 'yellow', 'blue']
# # autopctの指定は浮動小数点で表示するもの
# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)
# plt.axis('equal')
# plt.show()

y = [2, 4, 6, 8, 10]
y2 = [10, 11, 12, 13, 14]
x = np.arange(5)

plt.plot(x, y, label='Y')
plt.plot(x, y2, label='Y2')
# 図形の線がどのどのデータを指しているかを表示してくれる
plt.legend()
plt.show()