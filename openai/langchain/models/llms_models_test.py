from langchain.llms import OpenAI

llm = OpenAI(model_name="text-davinci-003")
response = llm("ITエンジニアについて30文字で教えて。")
print(response)