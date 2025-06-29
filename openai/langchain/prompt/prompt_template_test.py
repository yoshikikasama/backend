# このように生成したプロンプトをLLMなどのモデルに入れることができます。
# 今回は、OpenAIが提供するLLMである「text-davinci-003」を用いて回答を生成してみましょう。


from langchain import PromptTemplate
from langchain.llms import OpenAI

template = """
{subject}について30文字で教えて。
"""

prompt = PromptTemplate(
		template=template,
    input_variables=["subject"]
)
prompt_text = prompt.format(subject="ITエンジニア")
print(prompt_text)

llm = OpenAI(model_name="text-davinci-003")
print(llm(prompt_text))