import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit 超入門")

# st.write("DatFrame")


# st.write("Display Image")
st.write("Progress bar")

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration{i + 1}")
    bar.progress(i+1)
    time.sleep(0.1)

# if st.checkbox('Show Image'):
#     img = Image.open('sample_image.png')
#     st.image(img, caption='test Image', use_column_width=True)

# text = st.text_input('あなたの趣味を教えてください。')
# f"あなたの趣味は{text}です。"

# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# "condition:", condition

# option = st.selectbox(
#     'あなたがすきな数字を教えてください。',
#     list(range(1,11))
# )

# 'あなたの好きな数字は、' ,option, 'です。'

# df = pd.DataFrame({
#     "1列目":[1,2,3,4],
#     "2列目":[10,20,30,40]
# })
# df = pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a','b','c'])
# st.line_chart(df)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69, 139.70],
#     columns=['lat','lon'])
# st.map(df)

# st.write(df)
# highlight_max　列または行の中で最大なものをハイライトする
# axis=0で列にハイライト、1で行にハイライト
# st.table 動的な表を作成
# st.dataframe(df.style.highlight_max(axis=0),width=300,height=300)
# st.table 静的な表を作成
# st.table(df.style.highlight_max(axis=0))

# st.markdown("""
# # 章

# ## 節

# ### 項

# ```python
# def test():
#     print('test')
# a = test()
# ```
# """)


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')



