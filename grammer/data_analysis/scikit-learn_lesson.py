import matplotlib.pyplot as plt
import pandas as pd
import sklearn.datasets
import sklearn.linear_model
import sklearn.model_selection

# bostonの住宅データを取得
boston = sklearn.datasets.load_boston()
X = boston.data
df = pd.DataFrame(X, columns=boston.feature_names)
print(df)
# bostonの住宅価格が入っている
y = boston.target
print(y)
# 訓練用とテスト用でデータを分ける、0.2とすると80%は訓練データ残りはテストデータに
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.2)
# 学習アルゴリズム
lr = sklearn.linear_model.LinearRegression()
# 学習実行
lr.fit(X_train, y_train)
# アルゴリズムの正当性確認
print(lr.score(X_test, y_test))
# アルゴリズムから予測データの生成
predicted = lr.predict(X)
# 表示
fig, ax = plt.subplots()
ax.scatter(y, predicted, edgecolors=(0, 0, 0))
ax.plot([y.min(), y.max()], [y.min(), y.max()], "k--", lw=4)
ax.set_xlabel("Measured")
ax.set_ylabel("Predicted")
plt.show()