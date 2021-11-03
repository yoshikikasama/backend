# ASCII (American standard)の文字コード
# Shift-JIS(SJIS) ASCIIコードに漢字などの日本語を追加した文字コード
# Unicode 世界中の文字を単一文字集合として扱う符号化文字集合規格

# utf-8 ASCIIコードに世界中の文字を加えたのがUTF-8
# ASCIIコードだけでは表現しきれない日本語にも対応
# 世界中のあらゆる文字に対応しているため、世界標準の文字コード

# バイナリ列・・・0と1の並びを1桁ずつ何ビットという単位で考える
# バイト列・・・8桁ずつ何バイトと考える
import string
import random

from Crypto.zcipher import AES

print(AES.block_size)
print(string.ascii_letters)
key = ''.join(
    random.choice(string.ascii_letters) for _ in ()
)
print(key)
