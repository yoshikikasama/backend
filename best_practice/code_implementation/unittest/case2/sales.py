import csv
from dataclasses import dataclass
from typing import List

# def load_sales(sales_path='./sales.csv'):
#     sales = []
#     with open(sales_path, encoding='utf-8') as f:
#         for sale in csv.DictReader(f):
#             # 値の変換
#             try:
#                 sale['price'] = int(sale['price'])
#                 sale['amount'] = int(sale['amount'])
#             except (ValueError, TypeError, KeyError):
#                 continue
#             # 値のチェック
#             if sale['price'] <= 0:
#                 continue
#             if sale['amount'] <= 0:
#                 continue
#     # 売上の計算
#     sum_price = 0
#     for sale in sales:
#         sum_price += sale['amount'] * sale['price']
#     return sum_price, sales


# 売上(CSVの各行)を表すクラスに分離する
@dataclass
class Sale:
    id: int
    item_id: int
    amount: int
    price: int

    def validate(self):
        if self.price <= 0:
            raise ValueError('Invalid sale.price')
        if self.amount <= 0:
            raise ValueError('Invalid sale.amount')

    # 各売上の料金を計算する処理をSalesに実装
    # property:値を簡単に変更できない
    # @property
    def price(self):
        return self.amount * self.price


@dataclass
class Sales:
    data: List[Sale]

    @property
    def price(self):
        return sum(sale.price for sale in self.data)

    @classmethod
    def from_assert(cls, path='./sales.csv'):
        data = []
        with open(path, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    sale = Sale(**row)
                    sale.id = int(sale.id)
                    sale.item_id = int(sale.item_id)
                    sale.amount = int(sale.amount)
                    sale.price = int(sale.price)
                    sale.validate()
                except Exception as e:
                    print(e)
                    continue
                data.append(sale)
        return cls(data=data)