import collections

d = {'apple': 4, 'banana': 3, 'pear': 1, 'orange': 2}
od = collections.OrderedDict(
    sorted(d.items(), key=lambda t: t[0])
    # sorted(d.items(), key=lambda t: t[1])
    # sorted(d.items(), key=lambda t: len(t[0]))
)
print(od)
od['cc'] = 100
print(od)
od = collections.OrderedDict(
    sorted(od.items(), key=lambda t: t[0]))
print(od)
