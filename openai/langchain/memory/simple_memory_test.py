# 以前のChainsの記事で紹介したコードなのですが、以前のコードからの差分として、SequentialChainの中に、
# SimpleMemoryというインスタンスを格納しています。このメモリの中には、「"time": "2030年"」というデータが格納されています。
# そして、ここで設定した「time」という変数をこの中で使っているChainで使用しています。

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.memory import SimpleMemory

llm = OpenAI(model_name="text-davinci-003")
prompt_1 = PromptTemplate(
    input_variables=["adjective", "job", "time"],
    template="{time}において、{adjective}{job}に一番オススメのプログラミング言語は?\nプログラミング言語：",
)
chain_1 = LLMChain(llm=llm, prompt=prompt_1, output_key="programming_language")

prompt_2 = PromptTemplate(
    input_variables=["programming_language", "time"],
    template="現在は{time}だとします。{programming_language}を学ぶためにやるべきことを3ステップで100文字で教えて。",
)
chain_2 = LLMChain(llm=llm, prompt=prompt_2, output_key="learning_step")

overall_chain = SequentialChain(
    chains=[chain_1, chain_2],
    input_variables=["adjective", "job"],
    output_variables=["programming_language", "learning_step"],
    verbose=True,
    memory=SimpleMemory(memories={"time": "2030年"}),
)
output = overall_chain({
    "adjective": "ベテランの",
    "job": "エンジニア",
})
print(output)