
# coding: utf-8

# In[3]:


#Q1
#BigMart Sales Data Visualization
import pandas as pd
bigmartsales_dataset = pd.read_csv('BigMartSalesData.csv')
#Filter the data for the year 2011 from the dataset
bigmartsales_dataset_2011 = bigmartsales_dataset[bigmartsales_dataset['Year'] == 2011]
bigmartsales_dataset_month = bigmartsales_dataset_2011.groupby(["Month"])['Amount'].sum().reset_index(name='Total Sales')
#plot the graph now - Simple Plot
import matplotlib.pyplot as plt
plt.plot(bigmartsales_dataset_month["Month"], bigmartsales_dataset_month['Total Sales'])
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Month vs Total Sales')
plt.legend()
plt.show()

#Upto 4 month total sales were up and down
#After 4 month most of the months it went gradually up and dropped again in the month of 11
#2 month - lowest sales


# In[4]:


#Q2
#plot the graph now - Bar Graph
import matplotlib.pyplot as plt
plt.bar(bigmartsales_dataset_month["Month"], bigmartsales_dataset_month['Total Sales'], color=['y'])
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.title('Month vs Total Sales')
plt.show()

#Bar Chart should be better compared to Simple plot in terms of clear visualization and also for comparison


# In[49]:


#Q3
import pandas as pd
bigmartsales_dataset = pd.read_csv('BigMartSalesData.csv')
bigmartsales_dataset_country = bigmartsales_dataset.groupby(["Country"])['Amount'].sum().reset_index(name='Total Sales')
bigmartsales_dataset_country

import matplotlib.pyplot as plt
x = round(bigmartsales_dataset_country["Total Sales"],2)
y = bigmartsales_dataset_country["Country"]
plt.pie(x, labels=y, startangle=90, shadow=True, counterclock = False, labeldistance=1.1, radius = 1.5, rotatelabels=True
       ,center=(0, 0), frame=True, explode=None, autopct='%.2f')
plt.legend(loc='upper right', bbox_to_anchor=(0.5, 0.5))
plt.show()
#Based on Piechart United Kingdom contributes highest towards sales


# In[52]:


#Q4
import pandas as pd
bigmartsales_dataset = pd.read_csv('BigMartSalesData.csv')
bigmartsales_dataset['Amount'].fillna(0, inplace=True)
import numpy as np
y = bigmartsales_dataset['Amount']
plt.xlabel("Invoice Amount")
plt.ylabel("Invoice Amount")
plt.scatter(y,y, color='y')
plt.show()

