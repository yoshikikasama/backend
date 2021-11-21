import collections

l = ['a', 'a', 'a', 'b', 'b', 'c']
c = collections.Counter()
for word in l:
    c[word] += 1
print(c)
# 一番多いものを表示する
print(c.most_common(1))
print(c.values())
print(sum(c.values()))

import re
with open('counter_lesson.py', 'r')as f:
    words = re.findall(r'\w+', f.read().lower())
    print(collections.Counter(words).most_common(20))