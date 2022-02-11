"""data analytics

データサイエンス・・・データから有用な情報・知識を引き出すための基本原理
データマイニング・・・データサイエンスに基づく方法を活用して、データから有用な情報、
　　　　　　　　　　　知識を引き出す方法論の集合
CRISP-DM(CRISPデータマイニングプロセス)・・・データマイニングにおける標準プロセスの一つ。
                   プロジェクトでDMを用いる際の効果的なプロセスを明示している。
データ分析・・・データから価値を見出すさまざまな手法またはその組み合わせ。
　　　　　　　　データマイニングはその手法の一つ。

numpy ・・・科学計算で用いられるライブラリ。多次元配列を高速に処理できる。
pandas・・・表データを扱うライブラリ。分析や機械学習の前処理などが簡単にできる。
"""
import numpy as np
import pandas as pd

# ベクトル(1次元配列)の作成
# data = np.array([1, 2, 3, 4, 5])
# print(data)
# 要素数
# print(data.size)
# 内積(1*1 + 2*2 + 3*3 + 4*4 + 5*5)
# print(np.dot(data, data))
# 行列(2次元配列)matrix
# data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# matrix = data.reshape(3, 3)
# print(matrix)

# PandasのSeriesオブジェクト
# data = pd.Series([1, 2, 3, 4, 5])
data = pd.Series(
    [1, 2, 3, 4, 5],
    index=['a', 'b', 'c', 'd', 'e']
    )
print(data)
