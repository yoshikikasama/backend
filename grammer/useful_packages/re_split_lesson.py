import re
# 正規表現・・・さまざまな文字をひとつの文字列で表現する方法
# ex)apple
# orange
# grape
# lemon
# 正規表現すると[a-z]+
# メタ文字・・・正規表現で使用する特殊文字
# .   ^   $   [   ]   *   +   ?   |   (   )


s = 'My name is Mike'

print(s.split())
# オブジェクト名 = re.compile(r'正規表現パターン文字列')
# \W+⇨英数字以外
# p = re.compile(r'\W+')
# print(p.split(s))
p = re.compile('(blue|white|red)')
print(p.sub('color', 'blue socks and red shoes'))
print(p.sub('color', 'blue socks and red shoes', count=1))


def hexrepl(match):
    value = int(match.group())
    return hex(value)


p = re.compile(r'\d')
print(p.sub(hexrepl, '1234 55 11 test tesr'))