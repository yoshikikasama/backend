# フォーマットが誤っているときに、正しいフォーマットになるまで繰り返し修正をしてくれる機能もあります。
# この例では、クラスではなく、JSON形式のデータが入力されたときに、クラスの形式に変換をしてくれています。


from typing import List

from pydantic import BaseModel, Field

from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import (
    PydanticOutputParser,
    OutputFixingParser,
)

class Job(BaseModel):
    name: str = Field(description="Name of the job")
    skill_list: List[str] = Field(description="List of skills required for that job")

misformatted = "{'name': 'Frontend Engineer', 'skill_list': ['HTML', 'CSS', 'JS', 'TS']}"

parser = PydanticOutputParser(pydantic_object=Job)
print(parser)
print('\n')
new_parser = OutputFixingParser.from_llm(parser=parser, llm=ChatOpenAI(model_name="gpt-3.5-turbo"))
response = new_parser.parse(misformatted)
print(response)

