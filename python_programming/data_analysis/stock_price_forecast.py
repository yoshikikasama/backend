import matplotlib
import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas_datareader
import sklearn
import sklearn.linear_model
import sklearn.model_selection

df_appl = pandas_datareader.data.DataReader('AAPL', 'yahoo', '2021-01-01')
df_fb = pandas_datareader.data.DataReader('FB', 'yahoo', '2021-01-01')
df_gold = pandas_datareader.data.DataReader('GLD', 'yahoo', '2021-01-01')
# print(df_appl.tail(2))

# 統計学 Simple Moving Average
# df_appl['Close'] marketが閉じた時のappleの株価
# SMA 平均の株価の値段
df_appl['SMA'] = df_appl['Close'].rolling(window=14).mean()
df_appl['Close'].plot(figsize=(15, 6), color="red")
df_appl['SMA'].plot(figsize=(15, 6), color="green")

# データマイニング 様々なデータをみて、何か新しい予測を発掘する
# change マーケットが開けた時に何％株価が前日のclose時より下がったのか
df_appl['change'] = (((df_appl['Close'] - df_appl['Open'])) / (df_appl['Open']) * 100)
df_fb['change'] = (((df_fb['Close'] - df_fb['Open'])) / (df_fb['Open']) * 100)
df_gold['change'] = (((df_gold['Close'] - df_gold['Open'])) / (df_gold['Open']) * 100)
# print(df_appl.tail(2).round(2))

df_appl['Close'].plot(figsize=(15, 6), color="red")
df_fb['Close'].plot(figsize=(15, 6), color="blue")
df_gold['Close'].plot(figsize=(15, 6), color="orange")

# 機械学習(マシンラーニング)
df_appl['label'] = df_appl['Close'].shift(-30)
# print(df_appl.tail(40))

# ラベル行を削除したデータをxに代入
X = np.array(df_appl.drop(['label', 'SMA'], axis=1))
# 取りうる値の代償が著しく異なる特徴量を入れると結果が悪くなるため、
# 平均を引いて、標準偏差でわってスケーリングする
X = sklearn.preprocessing.scale(X)
# 予測に使う30日間のデータ
predict_data = X[-30:]
# 過去30日を取り除いた入力データ
X = X[:-30]
y = np.array(df_appl['label'])
# 過去30日を取り除いた正解ラベル
y = y[:-30]

# 訓練データ80% 検証データ 20%に分ける
# 第一引数に入力データ、第2引数に正解ラベルの配列
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
    X, y, test_size=0.2
)
# 訓練データを用いて学習する
lr = sklearn.linear_model.LinearRegression()
lr.fit(X_train, y_train)

# 検証データを用いて検証する,機械学習のスコア（正確性）をテストデータを用いて確かめる
accuracy = lr.score(X_test, y_test)

# 予測する
predicted_data = lr.predict(predict_data)

# 予測データの表示
df_appl['Predict'] = np.nan

last_date = df_appl.iloc[-1].name

one_day = 86400
next_unix = last_date.timestamp() + one_day

for data in predicted_data:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df_appl.loc[next_date] = np.append([np.nan]* (len(df_appl.columns)-1), data)

df_appl['Close'].plot(figsize=(15,6), color="green")
df_appl['Predict'].plot(figsize=(15,6), color="orange")
plt.show()