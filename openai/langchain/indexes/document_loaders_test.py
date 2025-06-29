# ここでは、PyPDFLoaderというライブラリを使って、最近発表された「フリーランス白書2023」のPDFをURLから読み込んでいます。
# そして、この後説明するvectorstoresというモジュールの中のChromaというツールを使って、『「フリーランスのリモートワークの実態」について教えて。』と検索しています。

from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

loader = PyPDFLoader("https://blog.freelance-jp.org/wp-content/uploads/2023/03/FreelanceSurvey2023.pdf")
pages = loader.load_and_split()
print(pages[0])

chroma_index = Chroma.from_documents(pages, OpenAIEmbeddings())
docs = chroma_index.similarity_search("「フリーランスのリモートワークの実態」について教えて。", k=2)
for doc in docs:
    print(str(doc.metadata["page"]) + ":", doc.page_content)