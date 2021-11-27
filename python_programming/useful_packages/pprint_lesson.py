import json
import pprint

l = ['apple', 'orange', 'banana', 'peach', 'mango']

l.insert(0, l[:])

pp = pprint.PrettyPrinter(indent=4, width=40)
# pp.pprint(l)
d = {'a': 'A', 'b': 'B', 'c': {'x': {'y': 'Y'}}}
print(json.dumps(d, indent=4))
