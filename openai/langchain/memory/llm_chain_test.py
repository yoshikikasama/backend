# 先ほどと同様に、ConversationBufferMemoryを格納するのですが、
# このときに「memory_key="chat_history"」と設定し、その変数をプロンプトテンプレートの中に入れ込みます。

from langchain.memory import ConversationBufferMemory
from langchain import OpenAI, LLMChain, PromptTemplate

template = """あなたは人間と話すチャットボットです。

{chat_history}
Human: {human_input}
Chatbot:
"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"],
    template=template
)
memory = ConversationBufferMemory(memory_key="chat_history")

llm_chain = LLMChain(
    llm=OpenAI(model_name="text-davinci-003"),
    prompt=prompt,
    verbose=True,
    memory=memory,
)

response = llm_chain.predict(human_input="AIとは何？")
print(response)
res = llm_chain.predict(human_input="より詳しく教えて。")
print(res)