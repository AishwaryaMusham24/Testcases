#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


import numpy as np


# In[5]:


import matplotlib.pyplot as plt


# In[7]:


fire_department = pd.read_csv("C:/test_cases/14.FDNY.csv")
fire_department


# In[17]:


df = pd.DataFrame(fire_department)
no_duplicates = df.drop_duplicates()
print(df)
print(no_duplicates)


# In[23]:


fire_dep = pd.read_csv("C:/test_cases/14.FDNY.csv",skiprows=1)
fire_dep


# In[25]:


fire_dep


# In[27]:


fire_dep.head()


# In[29]:


fire_dep.info()


# In[31]:


fire_dep.describe()


# In[32]:


fire_dep.isnull()


# In[34]:


fire_dep.columns


# In[35]:


fire_dep.index


# In[38]:


fire_dept = fire_dep[(fire_dep["FacilityAddress"]=="New York")]
fire_dept


# In[44]:


#Total number of records in a column
Number_of_columns = len(fire_dep["FacilityName"])
Number_of_columns


# In[45]:


total_records = len(df)
total_records


# In[48]:


#Total number of records in FacilityAddress
Number_of_records = len(fire_dep["FacilityAddress"])
Number_of_records


# In[49]:


#Total number of records in FacilityAddress
Number_of_records = len(fire_dep["Borough"])
Number_of_records


# In[51]:


fire_dep.info()


# In[54]:


facilities = df["Borough"]
facilities.info()


# In[56]:


borough_groups = df.groupby('Borough')
# Iterate through each group and display information
for Borough, group in borough_groups:
    print(f"Information for Borough: {Borough}")
    print(group)
    print("\n")


# In[59]:


#finding the manhattan data
filtered_data = df[df["Borough"]=="Manhattan"]
filtered_data


# In[61]:


#finding the information of manhattan data 
filtered_data.info()

