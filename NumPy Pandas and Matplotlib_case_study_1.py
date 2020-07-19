
# coding: utf-8

# In[70]:


#Q1
def seperatecolumn_numpyarr():
    import numpy as np
    salary, gender, age, PhD = np.genfromtxt('SalaryGender.csv', delimiter=',', skip_header=1, unpack=True)
    salary_arr = np.array(salary)
    gender_arr = np.array(gender)
    age_arr = np.array(age)
    phD_arr = np.array(PhD)
seperatecolumn_numpyarr()


# In[154]:


#Q2
def menwomen_phd():
    import pandas as pd
    df = pd.read_csv('SalaryGender.csv')
    phd_df = df.groupby(['Gender','PhD'])['Gender'].count().reset_index(name='Count')
    phd_df['Status'] = pd.Series(['FWOPHD','FWPHD','MWOPHD','MWPHD'])
    print(phd_df)
    female_count=0
    male_count=0
    for index,row in phd_df.iterrows():
        if(row['Gender'] == 0 and row['PhD'] == 1):
            female_count = row['Count']
        if(row['Gender'] == 1 and row['PhD'] == 1):
            male_count = row['Count']
    print('No of Males with PhD:', male_count)
    print('No of Females with PhD:', female_count)
menwomen_phd()


# In[168]:


#Q3
def no_phd():
    import pandas as pd
    df = pd.read_csv('SalaryGender.csv')
    age_phd = df[['Age','PhD']]
    age_phd = age_phd[(age_phd.PhD == 1)].reset_index(drop=True)
    print(age_phd.head(5))
no_phd()


# In[171]:


#Q4
def total_phd():
    import numpy as np
    import pandas as pd
    df = pd.read_csv('SalaryGender.csv')
    phd_df = df.groupby(['PhD'])['PhD'].count().reset_index(name='Count')
    phd_df['Status'] = pd.Series(['WOPHD','WPHD'])
    print(phd_df)
    count =0
    for index,row in phd_df.iterrows():
        if(row['PhD'] == 1):
            count = row['Count']
    print("Total Number of PhD Holders:",count)
total_phd()


# In[172]:


#Q5
def total_occurance():
    int_arr = [0,5,4,0,4,4,3,0,0,5,2,1,1,9]
    #bincount gives the occurances of each element in an array
    print(np.bincount(int_arr))
total_occurance()


# In[174]:


#Q6
def filter_greater5():
    import numpy as np
    np_arr = np.arange(0,12).reshape(4,3)
    result = np.array([each for each in np_arr.flatten() if each > 5])
    print(result)
filter_greater5()


# In[176]:


#Q7
def filter_NaN():
    import numpy as np
    arr = [np.nan, 1., 2.,np.nan, 3., 4., 5.]
    filter_arr=list(filter(lambda x :~np.isnan(x), arr))
    print(filter_arr)
filter_NaN()


# In[77]:


#Q8
def find_minmax():
    import numpy as np
    random_integer = np.random.random((10,10)) 
    random_integer_min, random_integer_max = random_integer.min(), random_integer.max()
    print('Minimum Value:', random_integer_min)
    print('Maximum Values:' , random_integer_max)
find_minmax()


# In[79]:


#Q9
def find_mean():
    import numpy as np
    random_integer = np.random.random((30))
    print('Mean Value:' , random_integer.mean())
find_mean()


# In[80]:


#Q10
def negate():
    import numpy as np
    arr_list = np.arange(0, 11)
    arr_list[(3 < arr_list) & (arr_list <= 8)] *= -1
    print(arr_list)
negate()


# In[81]:


#Q11
def column_sort():
    import numpy as np
    random_integer = np.random.random((3,3))
    random_integer = np.sort(random_integer, axis = 1)
    print('Column Sorting:', random_integer)
column_sort()


# In[178]:


#Q12
def axis_sum():
    import numpy as np
    random_integer = np.random.random((2,2,2,2))
    sum_axis = np.sum(random_integer, axis= tuple(range(random_integer.ndim-2,random_integer.ndim)))
    print ('Sum of last two axes', sum_axis)
axis_sum()


# In[218]:


#Q13
def swap():
    import numpy as np
    random_integer = np.random.random((4,3))
    ind = []
    for index,each in enumerate(random_integer):
        ind.append(index)
    print('Rows Before Swapping:', random_integer)
    random_integer = random_integer[ind[::-1]]
    print('Rows After Swapping:', random_integer)
swap()


# In[229]:


#Q14
def rank_matrix():
    import numpy as np
    random_arr = np.random.random((6,4))
    print(np.linalg.matrix_rank(random_arr))
rank_matrix()


# In[287]:


#Q15
#Phase1 - Data Collection
import pandas as pd
df = pd.read_csv('middle_tn_schools.csv')
df = df.fillna(0, axis=1)
df.describe()


# In[288]:


#Q15
#Phase 2 - Group by school_rating
df_rating = df.groupby('school_rating')
df_rating.describe()


# In[289]:


#Q15
#Phase 3 - Correlation analysis
correlation_matrix = df[['reduced_lunch', 'school_rating']].corr(method='pearson', min_periods=1)
print(correlation_matrix)


# In[300]:


#Q15
#Phase 4 - Scatter Plot
import matplotlib.pyplot as plt
plt.scatter(correlation_matrix['reduced_lunch'],correlation_matrix['school_rating'], c='r')
plt.xlabel("Reduced Lunch")
plt.ylabel("School Rating")
plt.xlim(-1,1.2)
plt.ylim(-1,1.2)
plt.legend()
plt.title("Reduced Lunch vs School Rating")
plt.show()


# In[293]:


#Q15
#Phase 5 - CorrelationMatrix
plt.matshow(df.corr())

