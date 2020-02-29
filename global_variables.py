# _*_ coding: utf-8 _*_

"""
Some useful global variables.

Author: Genpeng Xu
"""

import os


ROOT_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(ROOT_DIR, 'data')
USERDICT_FILEPATH = os.path.join(DATA_DIR, 'userdict.txt')
STOPWORDS_FILEPATH = os.path.join(DATA_DIR, 'stopwords.txt')
LABEL_2_TYPE_DICT_FILEPATH = os.path.join(DATA_DIR, 'label2type.joblib')
TYPE_2_LABEL_DICT_FILEPATH = os.path.join(DATA_DIR, 'type2label.joblib')
VECTORIZER_FILEPATH = os.path.join(DATA_DIR, 'vectorizer.joblib')
MODEL_FILEPATH = os.path.join(DATA_DIR, 'model.joblib')


if __name__ == '__main__':
    print(ROOT_DIR)
    print(DATA_DIR)
    print(USERDICT_FILEPATH)
    print(STOPWORDS_FILEPATH)
    print(LABEL_2_TYPE_DICT_FILEPATH)
    print(TYPE_2_LABEL_DICT_FILEPATH)
    print(VECTORIZER_FILEPATH)
    print(MODEL_FILEPATH)
