class Word():

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'test'

    def __len__(self):
        return len(self.text)


w = Word('a')
print(w)
print(len(w))
