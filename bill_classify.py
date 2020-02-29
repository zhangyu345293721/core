# _*_ coding: utf-8 _*_

"""
Classify bill by using machine learning algorithms.

Author: Genpeng Xu
"""

import re
import jieba
import joblib
import string
from zhon import hanzi
from typing import List, Set

# Own customized modules
from global_variables import *
from util import load_stopwords

jieba.load_userdict(USERDICT_FILEPATH)


# regular expression
PUNC_REGEX = r"^[{} \s]+$".format(string.punctuation + hanzi.punctuation)
NUM_REGEX = r"^[0-9]*\.?[0-9]+$"
UNIT_REGEX = r"^([0-9]*)(mm|cm|m)?$"
ALPHANUM_REGEX = r"^[a-zA-Z0-9]+$"

stopwords = load_stopwords(STOPWORDS_FILEPATH)
vectorizer = joblib.load(VECTORIZER_FILEPATH)
model = joblib.load(MODEL_FILEPATH)


def segment(text: str, stopwords: Set, lowercase: bool = True) -> str:
    if lowercase:
        text = text.lower()
    words = []
    jieba_res = jieba.cut(text)
    for w in jieba_res:
        if len(w) <= 1:
            continue
        if w in stopwords:
            continue
        if re.match(PUNC_REGEX, w):
            continue
        if re.match(NUM_REGEX, w):
            continue
        if re.match(UNIT_REGEX, w):
            continue
        words.append(w)
    return ' '.join(words)


def classify(texts: List[str]) -> List[int]:
    text_segmented = [segment(text, stopwords) for text in texts]
    return list(model.predict(vectorizer.transform(text_segmented)))

if __name__ == '__main__':
    label_2_type = joblib.load(LABEL_2_TYPE_DICT_FILEPATH)
    texts = [
        "零星砌砖 1.LC15陶粒混凝土填充层3.钢筋混凝土楼板扫水泥浆一道 4.部位:沉箱",
        "砌块墙 1.砌块品种、规格、强度等级:蒸压加气混凝土砌体 3.砂浆强度等级:预拌水泥砂浆M5.0 4.部位:变形缝"
    ]  # labels = ['围墙', '砌体及二次结构']
    labels = classify(texts)
    types = [label_2_type[label] for label in labels]
    print(types)
