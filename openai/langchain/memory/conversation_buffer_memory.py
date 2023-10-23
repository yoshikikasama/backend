# ConversationBufferMemoryのインスタンスは、save_contextというメソッドによって入力と出力を手動で書き込んだり、
# load_memory_variablesというメソッドによって読み込むこともできます。

from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = OpenAI(model_name="text-davinci-003")
conversation = ConversationChain(
    llm=llm,
    verbose=True,
    memory=ConversationBufferMemory()
)

response = conversation("AIとは何？")
print(response, "\n")
response = conversation("どのように使用できるか活用事例をあげてください。")
print(response)