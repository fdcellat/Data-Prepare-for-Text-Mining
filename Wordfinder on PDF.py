# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 13:02:53 2022

@author: fdcel
"""

import PyPDF2

# import necessary libraries
import pandas as pd
import os
import glob
  
# creating a pdf reader object
reader = PyPDF2.PdfReader(r'C:\Users\fdcel\pypdf\CV Eng.pdf')
path = os.getcwd()
pdf_files = glob.glob(os.path.join(path, "*.pdf"))

output = ""
for i in range(len(reader.pages)):
    pageObj = reader.pages[i]
    output += pageObj.extract_text()

################----------Dataframe ile dosya adı kelime ve kullanım sayısını sütunlar halinde verir -----###############
    
def wordfind(path_,word1,word2):
    word=[word1,word2]
    pdf_files = glob.glob(os.path.join(path_, "*.pdf"))
    column_names = ["Dosya_Adı","Kelime", "Kullanım_sayısı"]
    a = pd.DataFrame(columns = column_names)
    for f in pdf_files: 
        output = ""
        reader = PyPDF2.PdfReader(f)
        for i in range(len(reader.pages)):
            pageObj = reader.pages[i]
            output += pageObj.extract_text()
            output=output.lower()
        for i in word:
            a = a.append({'Dosya_Adı':str(f),'Kelime': str(i), 'Kullanım_sayısı':output.count(i)},ignore_index=True)
    return a        
  
    
wordfind(r'C:\Users\fdcel\pypdf','python','sql' )   
  
################----------Liste Şeklinde Verir -----###############
 
    
def wordfind(path_,word):
    pdf_files = glob.glob(os.path.join(path_, "*.pdf"))
    a=[]
    for f in pdf_files: 
        output = ""
        reader = PyPDF2.PdfReader(f)
        for i in range(len(reader.pages)):
            pageObj = reader.pages[i]
            output += pageObj.extract_text()
            output=output.lower()
        if output.count(word) > 0:# and output.count('sql')>0
            a.append(f)
    return a

wordfind(r'C:\Users\fdcel\pypdf','python')
