import re
# regular expression
"""
match() 文字列の先頭で正規表現とマッチするか判定
search() 文字列を操作して正規表現とどこにマッチするか調べる
findall() 正規表現にマッチする部分文字列を全て探し出しリストとして返す
finditer() 重複しないマッチオブジェクトのイテレータを返す
"""
# ドットは任意の1文字とmatch
m = re.match('a.c', 'adc')
# print(m)
# print(m.group())

# m = re.search('a.c', 'test abc test')
# print(m)
# print(m.span())

# m = re.findall('a.c', 'test abc test abc')
# print(m)

# m = re.finditer('a.c', 'test abc test abc')
# print([w.group() for w in m])
# # ?:bが0~1回
# m = re.match('ab?', 'a')
# print(m)
# # *:bが0回以上の繰り返し
# m = re.match('ab*', 'abbb')
# print(m)

# # +:bが1回以上の繰り返し
# m = re.match('ab+', 'abbb')
# print(m)

# # {3}:bが3回繰り返し
# m = re.match('ab{3}', 'abbb')
# print(m)

# # 小文字と大文字のmatch
# m = re.match('[a-zA-Z0-9_]', '_')
# m = re.match('[^a-zA-Z0-9_]', '_')
# print(m)

# # 任意の英数字とバックスラッシュのmatch
# m = re.match('\w', 'z')
# print(m)

# # 英数文字以外のmatch
# m = re.match('\W', '@')
# print(m)

# 数文字のmatch
# m = re.match('\d', '1')
# m = re.match('\D', 'a')
# print(m)

# m = re.match('a|b', 'b')
# m = re.match('(abc)+', 'abc')
# print(m)
# 空白とmatch
# m = re.match('\S', ' ')
# m = re.match('\s', ' ')
# print(m)
# 先頭がhitするか
m = re.search('^abc', 'abctest')
m = re.search('abc$', 'abctest abc')
print(m)
