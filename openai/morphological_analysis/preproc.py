import MeCab as mecab
import pickle
import numpy as np

with open("the_night_of_the_milky_way_train.pickle", mode="rb") as f:
    milky = pickle.load(f)

m_tagger = mecab.Tagger()
result = m_tagger.parse(milky)
print(result)

part_of_speech = "名詞"

noun_list = []
m_parse = m_tagger.parseToNode(milky)
while m_parse:
    if m_parse.feature.split(",")[0] == part_of_speech:
        noun_list.append(m_parse.surface)
    m_parse = m_parse.next

print(noun_list)
print(len(noun_list))
