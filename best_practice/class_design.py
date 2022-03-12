"""クラス設計


"""
# クラス設計
# 特定のキーを持つ辞書を期待するならクラスを定義する
import json
from dataclasses import dataclass
from datetime import date


@dataclass
class User:
    last_name: str
    first_name: str
    birthday: date

    # クラスにすることで、それぞれの処理をメソッドやプロパティーとして実装できる。
    # user.fullnameのように簡潔にプログラムを書ける
    @property
    def fullname(self):
        return self.last_name + self.first_name

    @property
    def age(self):
        today = date.today()
        born = self.birthday
        age = today.year - born.year
        if (today.month, today.day) < (born.month, born.day):
            return age - 1
        else:
            return age


def load_user():
    with open('./user.json', encoding='utf-8') as f:
        return User(**json.load(f))