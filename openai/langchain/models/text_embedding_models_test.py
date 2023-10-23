from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
query_result = embeddings.embed_query("ITエンジニアについて30文字で教えて。")

print(query_result)