#!/usr/bin/env python
# coding: utf-8

# 2023-09-16: Fall 2023 CAP_5610_ML HW-1 - Q2\Ch796193

# Importing the Numpy library

# In[18]:


import numpy as np


# Taking input from user for the length of the random vector

# In[19]:


k=int(input("Enter the length of the random vector we want to generate: "))  


# In[20]:


a = np.random.rand(k)  
#a= np.array([1,2,4,3,0,0,0])


# In[21]:


a


# In[22]:


b = np.random.rand(k) 
#b= np.array([6,7,8,9,5,5,5])


# In[23]:


b


# Correlation using Numpy - rounded the result to 4 decimal places

# In[24]:


Correlation_Numpy = round(np.corrcoef(a,b)[0,1],4)


# Cosine Similary using Numpy - rounded the result to 4 decimal places

# In[25]:


Cosine_simularity_Numpy = round((np.dot(a,b))/((np.linalg.norm(a))*(np.linalg.norm(b))),4)


# Euclidean Distance using Numpy - rounded the result to 4 decimal places

# In[26]:


Euclidean_Distance_Numpy = round(np.linalg.norm(a - b),4)


# In[27]:


Results = f'Numpy Correlation: {Correlation_Numpy}\nNumpy Cosine similarity: {Cosine_simularity_Numpy}\nNumpy Euclidean Distance: {Euclidean_Distance_Numpy}'


# Results from Numpy printed in array format

# In[28]:


print(Results)


# 

# End of the question 2 with Numpy

# Thank you
