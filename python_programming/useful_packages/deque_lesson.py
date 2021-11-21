import collections
import queue

# Double-end queue FIFO LIFO両方可能 メモリを効率的に使用するので推奨
collections.deque

q  = queue.Queue()
# [0, 1, 2]
lq = queue.LifoQueue()
l = []
d = collections.deque()

for i in range(3):
    q.put(i)
    lq.put(i)
    l.append(i)
    d.append(i)

# for _ in range(3):
#     print(f'FIFO queue = {q.get()}')
#     print(f'LIFO queue = {lq.get()}')
#     print(f'List       = {l.pop()}')
#     print(f'dequeue    = {d.popleft()}')
#     # print(f'dequeue    = {d.pop()}')
#     print()

# print(d[1])
print(d)
d.extendleft('x')
print(d)
d.extend('y')
print(d)
d.clear()
print(d)
# d.rotate()
# print(d)
# d.rotate()
