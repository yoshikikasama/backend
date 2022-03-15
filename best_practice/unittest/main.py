import hashlib


def calc_md5(content):
    # 空白文字の削除
    content = content.strip()
    m = hashlib.md5()
    m.update(content.encode('utf-8'))
    # ハッシュ値を求める
    return m.hexdigest()


def validate(text):
    return 0 < len(text) <= 100