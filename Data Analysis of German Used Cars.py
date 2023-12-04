#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Membaca dataframe

import pandas as pd

pd.set_option('display.max_rows',None)

pd.set_option('display.max_columns',None)

pd.set_option('display.width',None)

df = pd.read_excel('/Users/jeffrygunawan/Library/Mobile Documents/com~apple~CloudDocs/JEFFRY/Data Analysis/Kaggel Data Set/Germany Used Cars Dataset 2023/1. Data Excel Yang Sudah Clean/Cleaned For Excel.xlsx')

df.head(10)


# In[4]:


# check data NAN

df.isna().sum()


# In[5]:


# hapus semua NAN

df = df.dropna()


# In[6]:


# check data NAN

df.isna().sum()


# In[12]:


# Question: Retrieve all columns for cars with a registration year of 1995.

df[df['registration_year']==1995]


# In[18]:


# Question: Retrieve the unique colors available in the dataset.

print(df['color'].unique())


# In[24]:


# Question: Find the average power in kilowatts for cars with a transmission type of 'Manual'.

manual_cars = df[df['transmission_type'] == 'Manual']

average_power_kw = manual_cars['power_kw'].mean()

print("Average Power in Kilowatts for Manual Cars:", average_power_kw)


# In[26]:


print("Average Power in Kilowatts for Manual Cars : ",df[df['transmission_type'] == 'Manual']['power_kw'].mean())


# In[27]:


# Question: Retrieve the top 5 most expensive cars (highest price) in the dataset.

df.sort_values(by = ['price_in_euro'],ascending = (False)).head(5)


# In[31]:


# Question: Calculate the total mileage for each brand in kilometers.

df.groupby(['brand'])['mileage_in_km'].size().reset_index(name = 'Total Mileage').sort_values(by = ['Total Mileage'],ascending = (False))


# In[34]:


# Question: Find the average fuel consumption in liters per 100 km for cars registered in 1996.

print("The Average Fuel Consumption in Liters Per 100 Km For Cars Registered In 1996 : ",df[df['registration_year'] == 1996]['fuel_consumption_l_100km'].mean())


# In[37]:


# Question: Retrieve the details of cars with power greater than 150 kW and fuel type 'Petrol'.

df[(df['power_kw'] > 150) & (df['fuel_type'] == 'Petrol')]


# In[42]:


# Question: Count the number of cars for each fuel type.

df.groupby(['fuel_type']).size().reset_index(name = 'Total Cars').sort_values(by = ['Total Cars'],ascending = (False))


# In[45]:


# Question: Find the minimum prices for each brand.

df.sort_values(by = ['price_in_euro'],ascending = (True)).head(1)


# In[46]:


# Question: Find the maximum prices for each brand.

df.sort_values(by = ['price_in_euro'],ascending = (False)).head(1)


# In[ ]:




