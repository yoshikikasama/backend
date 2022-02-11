"""
Json形式
{
    "employee":
    [
        {"id": 111, "name": "Mike"},
        {"id": 222, "name": "Nancy"}
    ]
}
"""

import json

j = {
    "employee":
    [
        {"id": 111, "name": "Mike"},
        {"id": 222, "name": "Nancy"}
    ]
}

print(j)
print('######')
# python scriptの中での読み書きはsが付く(json.dumps, json.loadds())
a = json.dumps(j)
print(json.loads(a))

with open('test.json', 'w') as f:
    # fileへの書き込みはjson.dumpを行う
    json.dump(j, f)

print('#######')

with open('test.json', 'r') as f:
    print(json.load(f))