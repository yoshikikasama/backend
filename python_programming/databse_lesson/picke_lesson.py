import pickle

class T():
    def __init__(self, name):
        self.name = name

data = {
    'a': [1, 2, 3],
    'b': ('test', 'test'),
    'c': {'key': 'value'},
    'd': T('test')
}
# write and binary
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('data.pickle', 'rb')as f:
    data_loaded = pickle.load(f)
    print(type(data_loaded['a']))
    print(type(data_loaded['b']))
    print(type(data_loaded['c']))
    print(type(data_loaded['d']))

# pythonでしか使用できないため、他の言語との互換性がない



