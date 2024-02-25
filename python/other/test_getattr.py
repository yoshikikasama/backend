"""
getattr(object, name, default)
"""


class hello():
    def __init__(self):
        self.x = 1
        self.y = 2

    def plus(self):
        return self.x + self.y

    def minus(self):
        return self.y - self.x

    def args(self, s):
        return "I got {}".format(s)


cl = hello()
# 変数
print(getattr(cl, "x"))
# メソッド
print(getattr(cl, "plus")())
print(getattr(cl, "minus")())
print(getattr(cl, "multi", "None"))
print(getattr(cl, "args")("Hello World"))
