# クラス変数
class Person():
    # class変数、object共通の値,全てのobjectで共有される
    kind = 'human'

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)


a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()


class T():
    words = []

    def add_word(self, word):
        self.words.append(word)


c = T()
c.add_word('add 1')
c.add_word('add 2')
print(c.words)
d = T()
d.add_word('add 3')
d.add_word('add 4')
print(d.words)