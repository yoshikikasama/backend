import os

s = """\
AAA
BBB
CCC
DDD
"""
# with open('test.txt', 'a') as f:
#     f.write(s)

# with open('test.txt', 'r') as f:
#     # while True:
#     #     chunk = 2
#     #     line = f.read(chunk)
#     #     print(line)
#     #     if not line:
#     #         break
#     print(f.tell())
#     print(f.read(1))
#     f.seek(5)
#     print(f.read(1))
#     f.seek(14)
#     print(f.read(1))
#     f.seek(30)
#     print(f.read(2))

with open('test.txt', 'w+') as f:
    print(f.read())
    f.seek(0)
    f.write('a')

print(os.path.isfile('test.txt'))
print(os.getcwd())
