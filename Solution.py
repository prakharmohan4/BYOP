#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install wordcloud')


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS


# In[6]:


df = pd.read_csv(r"C:\Users\Yogesh Arora\Downloads\moto.csv", encoding ="latin-1")


# In[7]:


comment_words = ''
stopwords = set(STOPWORDS)


# In[8]:


for val in df.Review_text:
     
    # typecaste each val to string
    val = str(val)
 
    # split the value
    tokens = val.split()
     
    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
     
    comment_words += " ".join(tokens)+" "
 
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(comment_words)


# In[9]:


plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
 
plt.show()


# In[10]:





# In[11]:





# In[ ]:




