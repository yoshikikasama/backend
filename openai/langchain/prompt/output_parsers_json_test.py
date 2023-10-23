# 例えば、生成系AIからの回答をカンマ区切りのリストで出力したいとします。
# このような場合は「CommaSeparatedListOutputParser」が便利です。
# 次のように、fomat_instructionsをクラスから取得して、テンプレートに代入することで簡単に出力方法を指定することができます。

from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI

output_parser = CommaSeparatedListOutputParser()
format_instructions = output_parser.get_format_instructions()
prompt = PromptTemplate(
    template="List five {subject}.\n{format_instructions}",
    input_variables=["subject"],
    partial_variables={"format_instructions": format_instructions}
)

llm = OpenAI(model_name="text-davinci-003")
_input = prompt.format(subject="Programming Language")
output = llm(_input)
response =  output_parser.parse(output)
print(response)
