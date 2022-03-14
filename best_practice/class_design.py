"""クラス設計

特定のキーを持つ辞書のデメリット
・特定のキーが存在しているかのcheckが必要になることがある。
・他の形式の辞書で使えない関数なので再利用性が低い。

クラスのメリット
・REPL(対話型実行環境)でインスタンスを表示するときに、クラス名が表示されるのでわかりやすい。
・isinstanceを使用してクラスのインスタンスであるかをcheckできる。
・型アノテーションをするときに指定したclassが引数に渡されるかをチェックできる。
・IDEで動的解析をするときにクラスの定義元にジャンプしたり、関数の入出力をクラスのインスタンスで制限できる。
・クラス名でコードを検索すれば、そのクラスが使われている処理をすぐに見つけられる。
・目安は特定のkeyを持つ辞書を使う関数が増えたときにクラスにする程度でいい。

■initでのデフォルト引数の初期化は引数が多いと冗長になるためinitではなく、dataclassを使用する。

■「事前に他のメソッドを呼び出して値を設定する必要がある」という設計は、値が変更したときに再度呼び出す必要があるため
　よくない。
"""
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
        # functool.lru_cache
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


# クラスメソッド
@dataclass
class Product:
    id: int
    name: str

    @classmethod
    def retrieve(cls, id: int):
        """データAPIから商品の情報を取得して、インスタンスとして返す
        """
        data = retrieve_product_detail(id)
        return cls(
            id=data['id'],
            name=data['name']
        )


# クラスメソッドにすることでProductクラスから値を取得する処理も使用できる。
product = Product.retrieve(1)