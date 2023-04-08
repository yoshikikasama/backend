# openai

## 学習

- temprature:

  - 0: 同じプロンプトを複数回送信した場合、モデルは常に同一または非常に類似した Completions を返すことになる。
  - 1: 同じプロンプトを複数回送信した場合、モデルは毎回異なる Completions を返すことになる。
  - 通常、目的の出力が明確に定義されているタスクでは、低い temprature を設定するのが最適です。
  - より高い temprature は、多様性や創造性が求められるタスクや、エンド ユーザーや人間の専門家が選択できるいくつかのバリエーションを生成したい場合に役立ちます。

- token: 単語、単語のチャンク、または単一の文字にすることができます。

## 実行方法

最初にターミナル上に環境変数を export します。

export OPENAI_API_KEY="sk-xxxx"

```python
import os
openai.api_key = os.environ["OPENAI_API_KEY"]
```

gpt-3.5-turbo を model として使用するには upgrade が必要そう

```
pip install --upgrade pip
```

実行文

```cmd
streamlit run app_chatgpt_test.py
```
