import collections

a = {'a': 'a', 'c': 'c', 'num': 0}
b = {'b': 'b', 'c': 'cc'}
c = {'b': 'bbbb', 'c': 'ccc'}


class DeepChainMap(collections.ChainMap):
    def __setitem__(self, key, value):
        for mapping in self.maps:
            if type(mapping[key]) is int and mapping[key] < value:
                mapping[key] = value
            return
        self.maps[0][key] = value


m = DeepChainMap(a, b, c)
m['num'] = -1
print(m['num'])
# print(a)
# a.update(b)
# print(a)

# m = collections.ChainMap(a, b, c)
# print(m)
# print(m.maps)
# # aのcが優先される
# print(m['c'])
# m.maps.reverse()
# print(m['c'])
# m.maps.insert(0, {'c': 'cccccc'})
# print(m.maps)
# print(m['c'])
# del m.maps[0]
# print(m.maps)
# print(m['c'])
