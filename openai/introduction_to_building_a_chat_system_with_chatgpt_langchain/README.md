# ChatGPT/Langchain によるチャットシステム構築入門

https://github.com/yoshidashingo/langchain-book/

## 2 章 プロンプトエンジニアリング

- ファインチューニング: 既存モデルに追加の学習をさせる。

- few-shot prompting: prompt でいくつかの例を与えることで、求める回答を得やすくする手法。

## 3 章 Chat Completions API

- tiktoken: 実行前に token 数を count することができる
- 日本語の場合は、英語よりも token 数が多いため token 数削減の目的として日本語よりも英語を使うのが望ましい。
- temprature: 0~2 の間の値で、大きいほど出力がランダムになり、小さいほど決定的になる。

- function calling:
  - 利用可能な関数を LLM に伝えておいて、LLM に関数を使いたいという判断をさせる機能。
  - LLM が使いたいと判断した関数を LLM の利用者側で python などで実行する。
  - ![image](https://github.com/yoshikikasama/python/assets/61643054/1d8da4a2-1cd4-4911-b3ed-22bed8d0de02)

## 4 章 Langchain の基礎

- Langchain: LLM を使ったアプリケーション開発に必要な部品を抽象化されたモジュールとして提供している。

## 5 章 Langchain の活用

- RAG(Retrieval Augmented Generation): 文書を OpenAI の Embeddings API などでベクトル化しておいて、入力にベクトルが近い文書を検索して context に含める手法。
- ベクトル化: テキストを数値の配列に変換すること。
- Data Connection の仕組み:
  - Document loaders: データソースからドキュメントを読み込み
  - Document transformers: ドキュメントに何らかの変換をかける。ある程度の長さでチャンクに分割するなど。
  - Text embedding models: ドキュメントをベクトル化する
  - Vector Stores: ベクトル化したドキュメントの保存先
  - Retrievers: 入力のテキストと関連するドキュメントを検索する

## 6 章 外部検索、履歴を踏まえた応答をする Web アプリの実装

- streamlit の挙動: web アプリにアクセスしたタイミングや入力欄などのウィジェットを操作したタイミングで python script が上から下まで実行され、その内容が画面に表示される。

streamlit run app.py --server.port 8080

## 7 章 Slackアプリ実装

- Momento Cache: Serverlessなcache service

```
sls plugin install -n serverless-python-requirements
sls plugin install -n serverless-dotenv-plugin
AWS_SDK_LOAD_CONFIG=true AWS_PROFILE=infa-role  sls deploy
```
