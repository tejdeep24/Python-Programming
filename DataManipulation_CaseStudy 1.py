
# coding: utf-8

# In[29]:


#Q1
import pandas as pd
hollywood_df = pd.read_csv('HollywoodMovies.csv')
hollywood_df_story_quest = hollywood_df[hollywood_df['Story']=='Quest']
hollywood_df_story_quest = hollywood_df_story_quest.filter(['Movie', 'RottenTomatoes']).reset_index(drop=True)
hollywood_df_story_quest = hollywood_df_story_quest[hollywood_df_story_quest['RottenTomatoes']==min(hollywood_df_story_quest['RottenTomatoes'])]
print('Highest Rated movie in Quest Story Type:', hollywood_df_story_quest['Movie'])


# In[43]:


#Q2
import pandas as pd
hollywood_df = pd.read_csv('HollywoodMovies.csv')
hollywood_df_genre = hollywood_df.groupby(['Genre'])['Movie'].count().reset_index(name = 'movie_count')
hollywood_df_genre = hollywood_df_genre[hollywood_df_genre['movie_count']==max(hollywood_df_genre['movie_count'])]
print('Greatest number of movie releases in:', max(hollywood_df_genre['Genre']))


# In[60]:


#Q3
import pandas as pd
hollywood_df = pd.read_csv('HollywoodMovies.csv')
hollywood_df['Budget'].fillna(0, inplace=True)
hollywood_df_budget = hollywood_df.sort_values('Budget', ascending=False)
hollywood_df_budget.head(5)['Movie']


# In[63]:


#Q4
import pandas as pd
hollywood_df = pd.read_csv('HollywoodMovies.csv')
hollywood_df
hollywood_df['Profitability'].fillna(0, inplace=True)
hollywood_df['RottenTomatoes'].fillna(0, inplace=True)
x = hollywood_df['Profitability']
y = hollywood_df['RottenTomatoes']
#plot the graph now - Simple Plot
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.xlabel('Profitability')
plt.ylabel('RottenTomatoes')
plt.title('Profitability vs RottenTomatoes')
plt.show()


# In[51]:


#Q5 - 5.1
import pandas as pd
data_dict = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
'female': [0, 1, 1, 0, 1],
'age': [42, 52, 36, 24, 73],
'preTestScore': [4, 24, 31, ".", "."],
'postTestScore': ["25,000", "94,000", 57, 62, 70]}
dataset = pd.DataFrame(data_dict)
dataset


# In[52]:


#5.2
dataset.to_csv('example.csv', index=False)


# In[53]:


#5.3
import pandas as pd
example_df = pd.read_csv('example.csv')
example_df


# In[54]:


#5.4
import pandas as pd
example_df = pd.read_csv('example.csv', header=None)
example_df


# In[55]:


#Question 5
import pandas as pd
example_df = pd.read_csv('example.csv', header='infer', index_col=[0,1])
example_df


# In[56]:


#5.6
import pandas as pd
example_df = pd.read_csv('example.csv', header=None)
example_df.isna()


# In[57]:


#5.7
import pandas as pd
example_df = pd.read_csv('example.csv', skiprows=range(1,4))
example_df


# In[27]:


#5.8
import pandas as pd
example_df = pd.read_csv('example.csv', delimiter=',')
example_df


# In[113]:


#Q6 - 6.1
import pandas as pd
import numpy as np 
my_list = ['Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat']
my_series = pd.Series(my_list)
#6.1 - a
print('Lower Case', my_series.str.lower())
#6.1 - b
print('Upper Case', my_series.str.upper())
#6.1 - c
print('Length of All Elements', my_series.str.len())


# In[116]:


#Q6 - 6.2
import pandas as pd
my_list = [' Atul', 'John ', ' jack ', 'Sam']
my_series = pd.Series(my_list)
#6.2 - a
print('Strip', my_series.str.strip())
#6.2 - b
print('Left Strip', my_series.str.lstrip())
#6.2 - c
print('Right Strip', my_series.str.rstrip())


# In[53]:


#Q6 - 6.3
import pandas as pd
import numpy as np
my_list = ['India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture']
my_series = pd.Series(my_list)
my_series = my_series.dropna()
my_series_split = []
for index, value in my_series.iteritems():
    my_series_split.append(value.split('_'))
#print(my_series_split)
#print(my_series_split[0])
arr = np.array(my_series_split)
print(arr.reshape(1,9))


# In[45]:


#Q6 - 6.4
import pandas as pd
import numpy as np
my_list = ['A', 'B', 'C', 'AabX', 'BacX','', np.nan, 'CABA', 'dog', 'cat']
my_series = pd.Series(my_list)
my_series.replace(['X', 'dog'],'XX-XXX',regex=True)


# In[24]:


#Q6 - 6.5
import pandas as pd
my_list = ['12', '-$10', '$10,000']
my_series = pd.Series(my_list)
print(my_series.str.replace('$', ''))


# In[72]:


#Q6 - 6.6
import pandas as pd
import numpy as np
my_list = ['india 1998', 'big country', np.nan]
my_series = pd.Series(my_list)
my_series = my_series.dropna()
my_series_reverse = []
for index, value in my_series.iteritems():
    my_series_reverse.append(value[::-1])
arr = np.array(my_series_reverse)
print(arr)


# In[50]:


#Q6 - 6.7
import pandas as pd
my_list = ['1', '2', '1a', '2b', '2003c']
my_series = pd.Series(my_list)
my_series = my_series.str.isalnum()
my_series


# In[55]:


#Q6 - 6.8
import pandas as pd
my_list = ['1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c']
my_series = pd.Series(my_list)
my_series_contain = my_series.str.contains('A')
my_series_contain


# In[56]:


#Q6 - 6.9
import pandas as pd
my_list = ['a', 'a|b', np.nan, 'a|c']
my_series = pd.Series(my_list)
my_series


# In[62]:


#Q6 - 6.10
import pandas as pd
data_dict1 = {'key': ['One', 'Two'], 'ltable': [1, 2]}
dataset1 = pd.DataFrame(data_dict1)
data_dict2 = {'key': ['One', 'Two'], 'rtable': [4, 5]}
dataset2 = pd.DataFrame(data_dict2)
dataset1.merge(dataset2 , on = 'key')

