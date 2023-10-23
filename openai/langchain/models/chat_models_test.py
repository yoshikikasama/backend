from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
)

chat = ChatOpenAI(model_name="gpt-3.5-turbo")
response = chat([
	SystemMessage(content="日本語で回答して。"),
	HumanMessage(content="ITエンジニアについて30文字で教えて。"),
])

print(response)
