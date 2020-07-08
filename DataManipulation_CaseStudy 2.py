
# coding: utf-8

# In[60]:


#Q1
import pandas as pd
salary_df = pd.read_csv('Salaries.csv')
salary_df = salary_df.fillna(0, axis=1)
salary_df_2011_totalpay = salary_df[salary_df['Year'] == 2011]['TotalPay']
salary_df_2014_totalpay = salary_df[salary_df['Year'] == 2014]['TotalPay']
sum_totalpay_2011 = round(sum(salary_df_2011_totalpay),2)
sum_totalpay_2014 = round(sum(salary_df_2014_totalpay),2)
increase_salarycost = round(sum_totalpay_2014 - sum_totalpay_2011, 2)
print('Total Increase in Salary Cost:', increase_salarycost)


# In[189]:


#Q2
import pandas as pd
salary_df = pd.read_csv('Salaries.csv')
salary_df = salary_df.fillna(0, axis=1)
salary_df_2014 = salary_df[salary_df['Year'] == 2014]
salary_df_2014_job = salary_df_2014.groupby(['JobTitle'])['JobTitle', 'TotalPay']
salary_df_2014_job_mean = salary_df_2014_job.mean().reset_index()
print('Highest Mean Salary:', salary_df_2014_job_mean.max())
print('Lowest Mean Salary:', salary_df_2014_job_mean.min())


# In[103]:


#Q3
import pandas as pd
salary_df = pd.read_csv('Salaries.csv')
salary_df = salary_df.fillna(0, axis=1)
salary_df_2014 = salary_df[salary_df['Year'] == 2014]
salary_df_2014_totalpay = salary_df[salary_df['Year'] == 2014]['TotalPay']
salary_df_2014_overpay = salary_df[salary_df['Year'] == 2014]['OvertimePay']
sum_overpay_2014 = round(sum(salary_df_2014_overpay),2)
sum_totalpay_2014 = round(sum(salary_df_2014_totalpay),2)
save_pay = round(sum_totalpay_2014 - sum_overpay_2014, 2)
print('Money Save:', save_pay)


# In[155]:


#Q4
import pandas as pd
salary_df = pd.read_csv('Salaries.csv')
salary_df = salary_df.fillna(0, axis=1)
salary_df_job = salary_df[salary_df['Year'] == 2014]
salary_df_job


# In[178]:


#Q5
import pandas as pd
salary_df = pd.read_csv('Salaries.csv')
salary_df = salary_df.fillna(0, axis=1)
salary_df_employee = salary_df.groupby(['Year'])['EmployeeName', 'TotalPay']
salary_df_employee.max().reset_index()

