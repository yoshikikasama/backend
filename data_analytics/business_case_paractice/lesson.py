import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

datas_path = "/Users/kasamayoshiki/Documents/tmp/datas"
train = pd.read_csv(datas_path + "/case1/train.csv")
test = pd.read_csv(datas_path + "/case1/test.csv")
sample = pd.read_csv(datas_path + "/case1/sample.csv", header=None)

# head() 先頭5行分を読み込む関数
# print(train.head(10))
# tail() 後ろ5行分を読み込む関数
# print(train.tail())
# 行数と列数を確認したい場合(行、列)
# print(train.shape)
# print(sample.head())
# 基本統計量を確認
# print(train.describe())
#                           y     soldout        kcal  payday  temperature
# count(何個値が入っているか)  207.000000  207.000000  166.000000    10.0   207.000000
# mean(平均値)               86.623188    0.449275  404.409639     1.0    19.252174
# std(標準偏差)              32.882448    0.498626   29.884641     0.0     8.611365
# min(最小値)                29.000000    0.000000  315.000000     1.0     1.200000
# 25%                       57.000000    0.000000  386.000000     1.0    11.550000
# 50%(中央値)                78.000000    0.000000  408.500000     1.0    19.800000
# 75%                       113.000000    1.000000  426.000000     1.0    26.100000
# max(最大値)                171.000000    1.000000  462.000000     1.0    34.600000

# データの型の確認
# print(train.info())
# #   Column         Non-Null Count  Dtype  
# ---  ------         --------------  -----  
#  0   datetime       207 non-null    object (文字列)
#  1   y              207 non-null    int64  
#  2   week           207 non-null    object 
#  3   soldout        207 non-null    int64  
#  4   name           207 non-null    object 
#  5   kcal           166 non-null    float64
#  6   remarks        21 non-null     object 
#  7   event          14 non-null     object 
#  8   payday         10 non-null     float64
#  9   weather        207 non-null    object 
#  10  precipitation  207 non-null    object 
#  11  temperature    207 non-null    float64
# dtypes: float64(3), int64(2), object(7)

# 1つのカラムにだけ注目
# print(train['y'])
# yの平均値、中央値
# print(train['y'].mean())
# print(train['y'].median())
# yの値が150以上のデータのみ
# print(train[train['y'] >= 150])
# 曜日が月曜日のデータ
# print(train[train['week'] == '月'])
# 曜日が火曜日となっているデータをyで昇順・降順にする
# print(train[train['week'] == '火'].sort_values(by='y'))
# print(train[train['week'] == '火'].sort_values(by='y', ascending=False))
# 曜日が月曜日の時のyの平均値
# print(train[train['week'] == '月']['y'].mean())
# trainのtemperatureが平均以上のデータ
# print(train[train['temperature'] >= train['temperature'].mean()])
# yとweek2つのカラムの選択
# print(train[['y', 'week']])

# trainのyの折れ線ブラフ
# ax = train['y'].plot(figsize=(12, 4), title='graph')
# ax.set_xlabel('time')
# ax.set_ylabel('y')
# plt.show()

# ヒストグラム
# 横軸の階級・・・数値の幅がどれくらいなのか
# 縦軸の度数・・・数値の範囲がどれくらい該当するものがあるのか
# train['y'].plot.hist(grid=True)
# plt.axvline(x=train['y'].mean(), color='red')
# train['y'].plot.hist(figsize=(12, 4), title='histgram')
# plt.savefig('sample_fig.png')
# plt.show()