#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('survey_results_public.csv', index_col = 'Respondent')
schema_df =pd.read_csv('survey_results_schema.csv', index_col = 'Column')


# In[3]:


pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)


# In[4]:


df.head()


# In[5]:


schema_df


# In[6]:


df['ConvertedComp']


# In[7]:


# lests try to look at some methods and functions

df['ConvertedComp'].median()


# In[8]:


df.median()   # will check all the columns and get median of them


# In[9]:


# to get an overview of owr data we can use describe method

df.describe()


# In[10]:


df['ConvertedComp'].describe()


# In[11]:


# counts a non NaN values
df.count().head()


# In[12]:


df['SocialMedia']


# In[13]:


schema_df.loc['SocialMedia']


# In[14]:


# lets get some more out of the data

df['SocialMedia'].value_counts()


# In[15]:


# get the result in percentage
df['SocialMedia'].value_counts(normalize=True)


# In[16]:


df['Country'].count()


# In[17]:


df['Country'].value_counts()


# In[18]:


# lets try to group them by country
# to avoid unnecessary repetion lets name it country_group

country_group = df.groupby(['Country'])


# In[19]:


# from the grouped object get the specific group

country_group.get_group('United States').head()


# In[20]:


# but also we can use a filter

fltr = (df['Country'] == 'United States')

df.loc[fltr].head()


# In[21]:


# to get specific data on one of the countries
# social media popularity

fltr = (df['Country'] == 'United States')
df.loc[fltr]['SocialMedia'].value_counts()


# In[22]:


# but with grouping easy to get the specific info for all countries
country_group['SocialMedia'].value_counts().head(25)


# In[23]:


# so for specific country 

country_group['SocialMedia'].value_counts().loc['Canada']


# In[24]:


# just another filter to practice

filter2 = (df['SocialMedia'] == 'Reddit')
df[filter2]['Country'].value_counts()


# In[25]:


country_group['ConvertedComp'].describe()


# In[26]:


country_group['ConvertedComp'].describe().loc[['Ethiopia']]


# In[27]:


country_group['ConvertedComp'].median().loc['Ethiopia']


# In[28]:


# to get multiple functions result like mean and median from aur specific data 
# use agg() method

country_group['ConvertedComp'].agg(['mean', 'median']).loc['Ethiopia']


# In[29]:


# to see how many of them use python in ethiopia

filter2 = df['Country'] == 'Ethiopia'


# In[30]:


df[filter2]['LanguageWorkedWith'].str.contains('Python')


# In[31]:


df[filter2]['LanguageWorkedWith'].str.contains('Python').value_counts()


# In[32]:


df[filter2]['LanguageWorkedWith'].str.contains('Python').sum()


# In[33]:


# how many people know python in each country

country_group


# In[34]:


country_group['LanguageWorkedWith']


# In[35]:


# as country_group['LanguageWorkedWith'] is a SeriesGroupBy object we cant use str class directly
# lets use apply() method instead
# to check how many people know python in each country


# this lambda function gives us a series
# x is now the series


country_group['LanguageWorkedWith'].apply(lambda x: x)
   


# In[36]:


# is the same like this one 

df['LanguageWorkedWith']


# In[37]:


# sa apply str class on the series x now

country_group['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())


# In[38]:


# now lets try to find the percentage of python users in each country
# first get the users of python in each country

python = country_group['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum()).rename('python')

# it would be named as LanguageWorkedWith ,we have to rename it
# as thier name is identical , rename it here in firt place


# In[39]:


python


# In[40]:


all_progr_lan = country_group['LanguageWorkedWith'].count()


# In[41]:


all_progr_lan


# In[42]:


# concatenate the abave two series in one to form a dataframe
# use axis='columns' or axis = 1, to combine them in columns and create a dataframe 

python_df = pd.concat([python, all_progr_lan], axis = 'columns')


# In[43]:


python_df  # this is the dataframe


# In[44]:


# just swap the columns

 
python_df = python_df.reindex(columns=["LanguageWorkedWith","python"])


# In[45]:


python_df


# In[46]:


# lets add a column that has percentages of each country

python_df['percentage'] = python_df['python']/(python_df['LanguageWorkedWith'])*100


# In[47]:


python_df


# In[48]:


python_df.sort_values(by='percentage', ascending=False, inplace=True)


# In[49]:


python_df


# In[ ]:




