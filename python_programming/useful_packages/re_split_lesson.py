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
p = re.compile(r'\W+')
print(p.split(s))
