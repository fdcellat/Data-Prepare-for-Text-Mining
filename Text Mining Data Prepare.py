# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 23:20:25 2022

@author: fdcel
"""


#Boşlukları siler-------------------------------------------------------------
# Create text
text_data = [" Interrobang. By Aishwarya Henriette ",
 "Parking And Going. By Karl Gautier",
 " Today Is The night. By Jarek Prakash "]
# Strip whitespaces
strip_whitespace = [string.strip() for string in text_data]

#noktalama silme--------------------------------------------------------------
# Remove periods
remove_periods = [string.replace(".", "") for string in strip_whitespace]

#Büüyük Harfe çevirme----------------------------------------------------------
def capitalizer(string: str) -> str:
 return string.upper()
# Apply function

#** result = list(map(capitalizer, remove_periods))

#**result2 = list(map(lambda x:x.upper(), remove_periods))

#Tüm datayı istenen X ile değiştirme
import re
def replace_letters_with_X(string: str) -> str:
 return re.sub(r"[a-zA-Z]", "X", string)

result2 = list(map(replace_letters_with_X, remove_periods))

#HTML kodu okunabilir hale getirme---------------------------------------------
# Load library
from bs4 import BeautifulSoup
# Create some HTML code
html = """
 <div class='full_name'><span style='font-weight:bold'>
 Masego</span> Azra</div>"
 """
# Parse html
soup = BeautifulSoup(html, "lxml")
# Find the div with the class "full_name", show text
soup.find("div", { "class" : "full_name" }).text

#Noktalama işaretlerini kaldırma ----------------------------------------------
# Load libraries
import unicodedata
import sys
# Create text
text_data = ['Hi!!!! I. Love. This. Song....',
 '10000% Agree!!!! #LoveIT',
 'Right?!?!']
# Create a dictionary of punctuation characters
punctuation = dict.fromkeys(i for i in range(sys.maxunicode)
 if unicodedata.category(chr(i)).startswith('P'))
# For each string, remove any punctuation characters
[string.translate(punctuation) for string in text_data]


#Cümleyi kelimelere ayırma-----------------------------------------------------
# Load library
# from nltk.tokenize import word_tokenize
import nltk
# Create text
string = "The science, []of today . is the? technology of tomorrow"
# Tokenize words
nltk.tokenize.word_tokenize(string)

#Cümleleri ayırma--------------------------------------------------------------
# Load library
from nltk.tokenize import sent_tokenize
# Create text
string = "The science of today is the technology of tomorrow. Tomorrow is today."
# Tokenize sentences
sent_tokenize(string)

#çok kullanılan gereksiz kelimeleri silme I ,am,the gibi-----------------------
from nltk import stopwords
nltk.download('stopwords')
# Create word tokens
tokenized_words = ['i','am','going','to','go','to','the', 'store','and','park']
# Load stop words
stop_words = stopwords.words('english')
# Remove stop words
[word for word in tokenized_words if word not in stop_words]

#kökleri kaldırma--------------------------------------------------------------
# Load library
from nltk.stem.porter import PorterStemmer
# Create word tokens
tokenized_words = ['i', 'am', 'humbled', 'by', 'this', 'traditional', 'meeting']

# Create stemmer
porter = PorterStemmer()
# Apply stemmer
[porter.stem(word) for word in tokenized_words]

#Kelimenin formunu verir verb tense vb grammer bilgisi-------------------------

# Load libraries
from nltk import pos_tag
from nltk import word_tokenize
# Create text
text_data = "Chris loved outdoor running"
# Use pre-trained part of speech tagger
text_tagged = pos_tag(word_tokenize(text_data))
text_tagged

# NNP Proper noun, singular
# NN Noun, singular or mass
# RB Adverb
# VBD Verb, past tense
# VBG Verb, gerund or present participle
# JJ Adjective
# PRP Personal pronoun
#ne işe yarıyor meçhul---------------------------------------------------------
from sklearn.preprocessing import MultiLabelBinarizer
# Create text
tweets = ["I am eating a burrito for breakfast",
 "Political science is an amazing field",
 "San Francisco is an awesome city"]
# Create list
tagged_tweets = []
# Tag each word and each tweet
for tweet in tweets:
 tweet_tag = nltk.pos_tag(word_tokenize(tweet))
 tagged_tweets.append([tag for word, tag in tweet_tag])
# Use one-hot encoding to convert the tags into features
one_hot_multi = MultiLabelBinarizer()
one_hot_multi.fit_transform(tagged_tweets)
# kelime sayısı matrisi -------------------------------------------------------
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
# Create text
text_data = np.array(['I love Brazil. Brazil!',
 'Sweden is best',
'Germany beats both'])
# Create the bag of words feature matrix
count = CountVectorizer()
bag_of_words = count.fit_transform(text_data)

b=pd.DataFrame(bag_of_words.toarray(),columns=count.get_feature_names())

# idf kelime ağırlık matrisi oluşturma-----------------------------------------

# Load libraries
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
# Create text
text_data = np.array(['I love Brazil. Brazil!',
 'Sweden is best',
'Germany beats both'])
# Create the tf-idf feature matrix
tfidf = TfidfVectorizer()
feature_matrix = tfidf.fit_transform(text_data)
# Show tf-idf feature matrix
feature_matrix

a=feature_matrix.toarray()
