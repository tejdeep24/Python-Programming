
# coding: utf-8

# In[22]:


#Q1
import pandas as pd
hurricanes_dataset = pd.read_csv('Hurricanes.csv')
#print(hurricanes_dataset)
#Matplotlib
import matplotlib.pyplot as plot
#Bar Graph
year=hurricanes_dataset.Year
num_huricannes=hurricanes_dataset.Hurricanes
plot.bar(year,num_huricannes,color=['b','g'])
plot.show()


# In[143]:


#Q2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
city_df = pd.read_csv("CityTemps.csv")
city_df = city_df.drop(['Melbourne'],axis=1)
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.title("CityTemperature Analysis")
for year,subset in city_df.groupby('Year'):
    plt.plot(subset['Month'],subset['Moscow'],label =['Moscow',year])
    plt.plot(subset['Month'],subset['San Francisco'],label = ['San Francisco',year])
plt.legend()
plt.show()


# In[31]:


#Q3
import pandas as pd
dataset= pd.read_csv('data_file.txt')
#Store the data in new file – account_dataset.csv
dataset.to_csv('account_dataset.csv', index=False)
account_dataset = pd.read_csv('account_dataset.csv')
account_dataset = pd.DataFrame(account_dataset)


# In[47]:


#Q4
#Q5.1
import matplotlib.pyplot as plt
x = [1,2,3,4] 
y = [20, 21, 20.5, 20.8]
plt.plot(x,y)
plt.show()


# In[48]:


#Q5.2
import matplotlib.pyplot as plt
x = [1,2,3,4] 
y = [20, 21, 20.5, 20.8]
plt.plot(x, y, color='green', linestyle='dashed', marker='^',
         markerfacecolor='blue', markersize=12)
plt.show()


# In[58]:


#Q5.3
import matplotlib.pyplot as plt
x = [1,2,3,4] 
y = [20, 21, 20.5, 20.8]
plt.plot(x,y)
plt.xlabel("This is the X Axis")
plt.ylabel("This is the Y Axis")
plt.show()


# In[55]:


#Q5.4
import matplotlib.pyplot as plt
x = [1,2,3,4] 
y = [20, 21, 20.5, 20.8]
plt.plot(x,y)
plt.title("PersonWeight")
plt.xlabel("Person")
plt.ylabel("Weight")
plt.show()


# In[60]:


#Q5.5
import matplotlib.pyplot as plt
x = [1,2,3,4] 
y = [20, 21, 20.5, 20.8]
y_error = [0.12, 0.13, 0.2, 0.1]
plt.style.use('seaborn-whitegrid')
plt.errorbar(x, y, y_error);
plt.show()


# In[61]:


#Q5.6
import matplotlib.pyplot as plt
x = [1,2,3,4] 
y = [20, 21, 20.5, 20.8]
plt.plot(x,y)
plt.figure(figsize=(4,5))
plt.show()
plt.savefig('my_fig.png', dpi=100)


# In[64]:


#Q5.7
import matplotlib.pyplot as plt
x = [1,2,3,4] 
y = [20, 21, 20.5, 20.8]
plt.rcParams.update({'font.size': 14})
plt.plot(x,y)
plt.title("PersonWeight")
plt.xlabel("Person")
plt.ylabel("Weight")
plt.show()


# In[114]:


#Q5.8
import matplotlib.pyplot as plt
import numpy as np
x = np.random.random(50) 
y = np.random.random(50)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.scatter(x,y)
plt.show()


# In[112]:


#5.9
import pandas as pd
data_dict = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
'female': [0, 1, 1, 0, 1],
'age': [42, 52, 36, 24, 73],
'preTestScore': [4, 24, 31, 2, 3],
'postTestScore': [25, 94, 57, 62, 70]}
dataset = pd.DataFrame([data_dict])


# In[144]:


#5.10
import matplotlib.pyplot as plt
import numpy as np
x = list(dataset.preTestScore.values.flatten())
y = list(dataset.age.values.flatten())
a = list(dataset.postTestScore.values.flatten())
b = list(dataset.age.values.flatten())

for each in [(x,y),(a,b)]:
    plt.scatter(x,y, c='y')
    plt.scatter(a,b, c='g')
plt.xlabel("Testscores")
plt.ylabel("Age")
plt.legend(['preTestScores', 'postTestScores'])
plt.title("TestScores vs Age")
plt.show()

