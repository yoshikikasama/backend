import numpy as np
import pandas as pd
import pandas_datareader

s = pd.Series([1, 2, np.nan])
print(s)
print(s[0])
print(s.sum())
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print(df)
print(df.dtypes)
df = pd.DataFrame(np.random.randn(6, 4), index=pd.date_range('20170101', periods=6), columns=['A', 'B', 'C', 'D'])
print(df)
print(df.head(1))
print(df.values)
print(df.describe())
print(df.T)
print(df.sort_values(by='B'))
s = pd.DataFrame(pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20170101', periods=6)))
df['E'] = s
print(df)
print(df.shift(1))
s = df.iloc[0]
print(s)
print(df.append(s))
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar'], 'B': np.random.randn(4)})
print(df)
print(df.groupby('A').sum())
# yahooのAPIを使用して指定したシンボル（アップル）の日付以降の株価データを取得
s = pandas_datareader.data.DataReader('AAPL', 'yahoo', '2021-12-01')
print(s)