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

from Crypto.Cipher import AES

# print(AES.block_size)
print(string.ascii_letters)
key = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)
# 初期ベクトル
iv = ''.join(
    random.choice(string.ascii_letters) for _ in range(AES.block_size)
)
key = key.encode('utf-8')
iv = iv.encode('utf-8')

# 'wb'はバイナリファイルへの書き込み
with open('plaintext', 'r') as f, open('enc.dat', 'wb') as e:
    plaintext = f.read()
    # AES.MODE_CBC ⇨暗号化アルゴリズム, intの2が入る
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padding_length = AES.block_size - len(plaintext) % AES.block_size
    plaintext += chr(padding_length) * padding_length
    plaintext = plaintext.encode('utf-8')
    # 暗号化
    cipher_text = cipher.encrypt(plaintext)
    e.write(cipher_text)

with open('enc.dat', 'rb') as f:
    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    # 複合化
    decrypted_text = cipher2.decrypt(f.read())
    print(decrypted_text[:decrypted_text[-1]].decode('utf-8'))


# cipher2 = AES.new(key, AES.MODE_CBC, iv)
# decrypted_text = cipher2.decrypt(cipher_text)
# print(decrypted_text)
# print(decrypted_text[-1])
# print(decrypted_text[:-decrypted_text[-1]])
