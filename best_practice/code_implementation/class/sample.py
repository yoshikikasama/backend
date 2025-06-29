# クラス設計
# 特定のキーを持つ辞書を期待するならクラスを定義する
import json
from dataclasses import dataclass
from datetime import date
from .dataapi import retrieve_product_detail


@dataclass
class User:
    username: str
    email: str
    last_name: str
    first_name: str
    birthday: date
    role: str
    mail_confirmed: bool = False

    # クラスにすることで、それぞれの処理をメソッドやプロパティーとして実装できる。
    # user.fullnameのように簡潔にプログラムを書ける
    @property
    def fullname(self):
        return self.last_name + self.first_name

    @property
    def age(self):
        # birthdayが変更される可能性があるため、age関数として作成
        # functool.lru_cacheを使ってpropertyの計算結果をメモリにキャッシュさせる。
        today = date.today()
        born = self.birthday
        age = today.year - born.year
        if (today.month, today.day) < (born.month, born.day):
            return age - 1
        else:
            return age


def load_user():
    with open("./user.json", encoding="utf-8") as f:
        return User(**json.load(f))


# クラスメソッド
@dataclass
class Product:
    id: int
    name: str

    @classmethod
    def retrieve(cls, id: int):
        """データAPIから商品の情報を取得して、インスタンスとして返す"""
        data = retrieve_product_detail(id)
        return cls(id=data["id"], name=data["name"])


# クラスメソッドにすることでProductクラスから値を取得する処理も使用できる。
product = Product.retrieve(1)
