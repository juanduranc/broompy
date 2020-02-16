#!/usr/bin/env python
# coding: utf-8

# <span style="color:green; font-size:25px"><b>Clean Assist, a Python Library</b></span><br><br>
# <span style="color:#45B39D; font-size:20px"><b>by: Juan Duran, Business Analyst & Industrial Engineer</b></span><br><br>
# 
# <span style="color:green; font-size:16px"><b>Description:</b></span><br>
# This is a code sample. Please visit: https://github.com/juanduranc/Clean-Assist for assistance on interpretation and usage.
# <hr style="border-top: 6px solid green;">

# In[17]:


import requests
url = 'https://raw.githubusercontent.com/juanduranc/Clean-Assist/master/library'
exec(requests.get(url).text)
help(clean_assist)


# In[9]:


# Dataset as sample
mpg = sns.load_dataset('mpg')
mpg.head(5)


# In[7]:


clean_assist.table(mpg, 30, 16)


# In[14]:


list_var = ['mpg','cylinders','displacement','weight','acceleration','model_year']
clean_assist.normality(mpg, list_var, 'n', 14, 36, 14)

