# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 13:51:19 2022

@author: fdcel
"""


import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
#from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import Word, TextBlob
from wordcloud import WordCloud
import nltk
nltk.download('wordnet')
sw = stopwords.words('english')
import googletrans
from deep_translator import GoogleTranslator

data=pd.read_excel(r'Path')

data.isnull().sum()

data=data.dropna(subset=['rawdata'])

def textmining(data,col):
    data[col] = data[col].apply(lambda x: GoogleTranslator(source='tr', target='en').translate(x))#you can change auto to your language
    data[col] = data[col].str.lower()
    data[col] = data[col].str.replace('[^\w\s]', '')
    data[col] = data[col].str.replace('\d', '')
    data[col] = data[col].apply(lambda x: " ".join(x for x in str(x).split() if x not in sw))
    data[col].apply(lambda x: TextBlob(x).words).head()
    data[col] = data[col].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
    tf = data[col].apply(lambda x: pd.value_counts(x.split(" "))).sum(axis=0).reset_index()
    tf.columns = ["words", "tf"]
    tf = tf.sort_values("tf", ascending = False).reset_index()
    return tf

tf=textmining(data,'rawdata')

tf['tr_word'] = tf['words'].apply(lambda x: GoogleTranslator(source='en', target='tr').translate(x))

tf.loc[tf['tf']>200]

matplotlib.rcParams['figure.figsize'] = (12.0, 8.0)
tf[tf["tf"] > 1000].plot.bar(x="words", y="tf")


text = " ".join(i for i in data['colname'])
wordcloud = WordCloud().generate(text)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()


wordcloud = WordCloud(max_font_size=50,
                      max_words=100,
                      background_color="white").generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

wordcloud.to_file("wordcloud.png")