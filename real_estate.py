#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


real_estate = pd.read_csv("C:/test_cases/12.real state.csv")
real_estate

real = pd.DataFrame(real_estate)
duplicates = real[real.duplicated()]
print(duplicates)
# In[5]:


real = pd.DataFrame(real_estate)
duplicates = real[real.duplicated()]
print(duplicates)


# In[6]:


no_duplicates = real.drop_duplicates()
no_duplicates


# In[7]:


real.isna


# In[8]:


real.isnull()


# In[9]:


real.describe()


# In[10]:


real.info()


# In[11]:


real.head()


# In[12]:


filtered_data = real[(real['type'] == 'villa') & (real['price'] >= 10000)]
filtered_data


# In[13]:


city_wise_villas = filtered_data.groupby('city')['type'].count().reset_index()
city_wise_villas.columns = ['city', 'Number of Villas']
city_wise_villas


# In[14]:


#finding the residential type in Galt city
filtered_city = real[(real['city']=='GALT') & (real['sq__ft'] > 800) & (real['type'] == 'Residential')]
result_df = filtered_city[['street', 'sq__ft', 'sale_date', 'city']]
print(result_df)


# In[22]:


#Finding the cheapest villa in a state CA
minimum_city = real[(real['type']=='villa') &(real['state']=='CA')]
minimum_value_of_villa = minimum_city[minimum_city['price']==minimum_city['price'].min()]
filtered = minimum_value_of_villa[['city', 'street', 'price', 'type']]
print(filtered)


# In[44]:


#finding the villa in between the range
#minimum_value = real[(real['price'] >= 60000) & (real['price'] <=120000)]
filter_extract = real[(real['price'] >= 60000) & (real['price'] <= 120000) & (real['sq__ft'] > 1450) & (real['beds'] >= 3) & (real['baths'] >= 2)]
sorted_df = filter_extract.sort_values('price')
# Display the top 5 matching residency details
top_residencies = sorted_df.head()
print(top_residencies)


# In[52]:


filtered_data = real[(real['type'] == 'Residential') & (real['beds'] > 2)]
grouped_data = filtered_data
result = grouped_data[['city', 'baths', 'sq__ft', 'price', 'type', 'beds']]
result


# In[ ]:




