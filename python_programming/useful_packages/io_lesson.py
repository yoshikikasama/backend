import io

with open('/tmp/a.txt', 'w') as f:
    f.write('test test')

with open('/tmp/a.txt', 'r') as f:
    print(f.read())

# ファイル操作のテストなどに使用
f = io.BytesIO()
f.write(b'string io test')
f.seek(0)
print(f.read())
