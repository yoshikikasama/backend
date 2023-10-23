# ここでは、GPT-4に関する文章に対して「split_text」というメソッドを用いて、「\n\n」（改行2つ）でテキスト分割を行なっています。
# そして、もう一つ条件として「chunk_size」を100に設定していることにより、テキスト分割された塊が100文字を超えないけど、なるべく大きい塊になるように結合されています。
# また、create_documentsというメソッドを使うと、文字列ではなく「document」というクラスの塊にできます。

from langchain.text_splitter import CharacterTextSplitter
long_text = """
GPT-4は、OpenAIが開発したAI技術であるGPTシリーズの第4世代目のモデルです。

自然言語処理(NLP)という技術を使い、文章の生成や理解を行うことができます。

これにより、人間と同じような文章を作成することが可能です。

GPT-4は、トランスフォーマーアーキテクチャに基づいており、より強力な性能を発揮します。

GPT-4は、インターネット上の大量のテキストデータを学習し、豊富な知識を持っています。

しかし、2021年9月までの情報しか持っていません。

このモデルは、質問応答や文章生成、文章要約など、様々なタスクで使用できます。

ただし、GPT-4は完璧ではありません。

時々、誤った情報や不適切な内容を生成することがあります。

使用者は、その限界を理解し、

適切な方法で利用することが重要です。
"""
print(len(long_text))

text_splitter = CharacterTextSplitter(
    separator = "\n\n",
    chunk_size = 100,
    chunk_overlap = 0,
    length_function = len,
)
text_list = text_splitter.split_text(long_text)
print("text_list:", text_list)
print("len(text_list[0]:):", len(text_list[0]))

document_list = text_splitter.create_documents([long_text])
print("document_list:", document_list)
print("len(document_list):", len(document_list))