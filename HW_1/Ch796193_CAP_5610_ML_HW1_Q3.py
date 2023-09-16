#!/usr/bin/env python
# coding: utf-8

# 2023-09-16: Fall 2023 CAP_5610_ML HW-1 - Q3\Ch796193

# Importing the Scipy and Numpy library

# In[2]:


import scipy as sp
import numpy as np
from scipy import stats


# Begining of Question 3 with Scipy

# Taking input from user for the length of the random vector

# In[3]:


k=int(input("Enter the length of the random vector we want to generate: "))  


# In[4]:


a = np.random.rand(k)  
#a= np.array([1,2,4,3,0,0,0])


# In[5]:


a


# In[6]:


b = np.random.rand(k) 
#b= np.array([6,7,8,9,5,5,5]) 


# In[7]:


b


# Correlation using Scipy

# In[8]:


#Correlation_scipy = round(sp.spatial.distance.correlation(a,b),4)
Correlation_scipy, p_val_scipy = stats.pearsonr(a,b)


# In[9]:


round(p_val_scipy,4)


# Cosine Similary using Scipy

# In[10]:


Cosine_simularity_Scipy = round(1 - sp.spatial.distance.cosine(a,b),4)


# Euclidean Distance using Scipy

# In[11]:


Euclidean_Distance_Scipy = round(sp.spatial.distance.euclidean(a,b),4)


# In[14]:


Results = f'Scipy Correlation: {round(Correlation_scipy, 4)}\nScipy Cosine similarity: {Cosine_simularity_Scipy}\nScipy Euclidean Distance: {Euclidean_Distance_Scipy}'


# Results from Numpy printed in array format

# In[16]:


print(Results)


# 

# End of Question 3 with Scipy

# Begining of Question 3 with Pandas - using same vectors a, b in the above code

# Importing the pandas library

# In[18]:


import pandas as pd


# making the pandas series of a, b

# In[19]:


a1 = pd.Series(a)
b1 = pd.Series(b)


# Correlation using Pandas

# In[20]:


correlation_pandas = a1.corr(b1)


# Print the correlation using Pandas

# In[22]:


print ("Pandas Correlation:",round(correlation_pandas,4))


# Please see, Cosine Similarity and Euclidean Distance are not directly defined as fucntions in the Pandas Library.

# End of Question 3 with Pandas

# Thank you
