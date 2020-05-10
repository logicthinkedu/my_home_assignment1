#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import pandas as pd
import numpy as np

import tensorflow.keras as keras
from tensorflow.keras.models import load_model
import tensorflow as tf

from flask import Flask, render_template, request


# # 导入词表

# In[2]:


import json
with open(r'dataset/word2idx.json', "r") as f:
    word2idx = json.load(f)


# In[3]:


max_word_length = 500
max_seq_length = 512


# # 导入模型

# In[4]:


textCNN_model = load_model(r'model_save/model.h5')

layer_output = textCNN_model.get_layer('concatenate').output
intermediate_model = tf.keras.models.Model(inputs=textCNN_model.input,outputs=layer_output)


# # 导入数据

# In[5]:


data = pd.read_csv(r'dataset/JD_dataset.csv',usecols = ['Query','Description'])
data.sample(10)


# # 文本预处理

# In[6]:


REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

def clean_text(text):
    text = text.replace(r'\\n', ' ').replace(r'\\r', ' ').replace(r'\r', ' ').replace(r'\n', ' ')
    text = cleanr.sub(' ', text)
    
    text = text.lower() # lowercase text
    text = REPLACE_BY_SPACE_RE.sub(' ', text) # replace REPLACE_BY_SPACE_RE symbols by space in text. substitute the matched string in REPLACE_BY_SPACE_RE with space.
    text = BAD_SYMBOLS_RE.sub('', text) # remove symbols which are in BAD_SYMBOLS_RE from text. substitute the matched string in BAD_SYMBOLS_RE with nothing. 

    text = ' '.join(word for word in text.split()) # remove stopwors from text
    return text

def string_process(l):
    return l.split()[:max_word_length]

data['Description'] = data['Description'].apply(clean_text)
data['word_list'] = data['Description'].apply( string_process )
data.sample(10)


# In[7]:


def PreProcessInputData( text ):
    word_labels = []

    for sequence in text:
        len_text = len(sequence)

        ###########################################
        temp_word_labels = []
        for w in sequence:
            temp_word_labels.append( word2idx.get( str(w).lower(),1 ) )

        ###########################################
        temp_word_labels = temp_word_labels + [0] * ( max_seq_length - len_text )
        word_labels.append( temp_word_labels )

    return word_labels


# # 简历转向量矩阵

# In[8]:


XX = np.array( PreProcessInputData( data['word_list'] ) )
intermediate_prediction = intermediate_model.predict( XX )

JD_Vector_List = []
for i in range(0,len(intermediate_prediction)):
    JD_Vector_List.append( intermediate_prediction[i][0][0] )


# In[ ]:





# # 用 FAISS 对向量矩阵做索引

# In[9]:


import numpy as np
import faiss                   # make faiss available

# 构造数据
import time
d = 500                           # dimension
nb = len(JD_Vector_List)                      # database size

np.random.seed(1234)             # make reproducible
xb = np.array( JD_Vector_List ).astype('float32')


# In[10]:


# %time index = faiss.IndexFlatL2(d)   # build the index
index = faiss.IndexFlatL2(d)   # build the index

print(index.is_trained)
index.add(xb)                  # add vectors to the index
print(index.ntotal)


# In[ ]:





# # 启动 Flask

# In[ ]:


app = Flask(__name__)

@app.route('/get_simmilar/', methods=['POST'])
# 返回最接近的向量
def get_simmilar():
    print( 'get_simmilar' )
    
    number = 5
    my_clean_text = clean_text( eval(request.get_data())['CV'] )
    print( my_clean_text )
    
    D, I = index.search( intermediate_model.predict( np.array( PreProcessInputData( [  my_clean_text.split()[:max_word_length] ] ) ) )[0][0] , number)
    
    # 返回最接近的职位描述
    response = {}
    for ind in I[0]:
        print('-'*120)
        print( data['Query'].iloc[ind] )
        print( data['Description'].iloc[ind] )
        response[str(ind)] = data['Description'].iloc[ind]
    
    return str(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3335)


# In[ ]:





# In[ ]:




