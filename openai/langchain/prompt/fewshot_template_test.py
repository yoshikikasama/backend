# 「FewShotPromptTemplate」とは、few-shot learning用のテンプレートで、次のようにJSON形式の教師データを簡単に入力できます。
# 教師データに加えて、教師データをどのようなフォーマットで学習させるかも指定できます。


from langchain import PromptTemplate
from langchain import FewShotPromptTemplate
from langchain.llms import OpenAI

examples = [
    {"fruit": "りんご", "color": "赤"},
    {"fruit": "キウイ", "color": "緑"},
    {"fruit": "ぶどう", "color": "紫"},
]

example_formatter_template = """
フルーツ: {fruit}
色: {color}\n
"""
example_prompt = PromptTemplate(
    template=example_formatter_template,
    input_variables=["fruit", "color"]
)

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="フルーツの色を漢字で教えて。",
    suffix="フルーツ: {input}\n色:",
    input_variables=["input"],
    example_separator="\n\n",

)

prompt_text = few_shot_prompt.format(input="オレンジ")
print(prompt_text)

llm = OpenAI(model_name="text-davinci-003")
print(llm(prompt_text))