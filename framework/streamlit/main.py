import streamlit as st
import numpy as np
import pandas as pd

st.title("Streamlit 超入門")

st.write("DatFrame")

df = pd.DataFrame({
    "1列目":[1,2,3,4],
    "2列目":[10,20,30,40]
})
# st.write(df)
# highlight_max　列または行の中で最大なものをハイライトする
# axis=0で列にハイライト、1で行にハイライト
# st.table 動的な表を作成
# st.dataframe(df.style.highlight_max(axis=0),width=300,height=300)
# st.table 静的な表を作成
# st.table(df.style.highlight_max(axis=0))

"""
# 章

## 節

### 項

```python
def test():
    print('test')
a = test()
```

"""



