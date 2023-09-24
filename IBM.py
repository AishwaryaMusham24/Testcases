#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


IBM_data = pd.read_csv("C:/test_cases/9.ibm.csv")
IBM_data


# In[5]:


IBM_data.isna


# In[6]:


IBM_data.isnull()


# In[7]:


IBM_data.info()


# In[8]:


IBM_data.head()


# In[9]:


IBM = pd.DataFrame(IBM_data)
no_duplicates = IBM.drop_duplicates()
no_duplicates


# In[10]:


IBM.columns


# In[11]:


IBM.index


# In[12]:


#Finding the employee number and dept of employee who does overtime
Employee = IBM[(IBM['OverTime'] == 'Yes')]
total = Employee[['EmployeeNumber', 'Department']]
total


# In[13]:


#Finding the last 5 employees based on last promotion received
IBM.sort_values(by='YearsSinceLastPromotion', ascending=False, inplace=True)
# Select the last 5 employees
last_5_employees = IBM.head(5)
print(last_5_employees)


# In[14]:


#Finding the list of employee whose income is more than the average income of all the employee’s present in the same department
avg_income_by_department = IBM.groupby('Department')['MonthlyIncome'].mean()
IBM['AvgIncomeInDepartment'] = IBM['Department'].map(avg_income_by_department)

# Filter employees whose income is greater than the average income in their department
high_income_employees = IBM[IBM['MonthlyIncome'] > IBM['AvgIncomeInDepartment']]

print(high_income_employees)


# In[15]:


max_income_index = IBM['MonthlyIncome'].idxmax()

# Get the row with the highest monthly income and select specific columns
employee_with_highest_income = IBM.loc[max_income_index, [
    'Age', 'Attrition', 'BusinessTravel', 'DailyRate', 'Department',
    'DistanceFromHome', 'Education', 'EducationField', 'EmployeeCount',
    'EmployeeNumber', 'EnvironmentSatisfaction', 'Gender', 'HourlyRate',
    'JobInvolvement', 'JobLevel', 'JobRole', 'JobSatisfaction',
    'MaritalStatus', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',
    'Over18', 'OverTime', 'PercentSalaryHike', 'PerformanceRating',
    'RelationshipSatisfaction', 'StandardHours', 'StockOptionLevel',
    'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance',
    'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion',
    'YearsWithCurrManager'
]]

print("Employee with the highest monthly income:")
print(employee_with_highest_income)


# In[16]:


#Show one scatter plot, it is your choice to show which two features you want to use, by using original dataset
plt.figure(figsize=(10, 6))
plt.scatter(IBM['Age'], IBM['MonthlyIncome'], alpha=0.5)
plt.title('Scatter Plot of Age vs Monthly Income')
plt.xlabel('Age')
plt.ylabel('Monthly Income')
plt.grid(True)
plt.show()


# In[ ]:




