
# coding: utf-8

# In[28]:


#import pandas
import pandas as pd

#Read All .csv files
df1=pd.read_csv('MathScoreTerm1.csv')
df2=pd.read_csv('DSScoreTerm1.csv')
df3=pd.read_csv('PhysicsScoreTerm1.csv')

#Drop 'name' and 'Ethinicity' columns
dataset1=df1.drop(['Name','Ethinicity'], axis=1)
dataset2=df2.drop(['Name','Ethinicity'], axis=1)
dataset3=df3.drop(['Name','Ethinicity'], axis=1)

#dataset1['Score'].fillna(0, inplace=True)
#dataset2['Score'].fillna(0, inplace=True)
#dataset3['Score'].fillna(0, inplace=True)

#Merge all datasets
ScoreFinal = pd.concat([dataset1, dataset2, dataset3], axis = 0)

#Change Sex(M/F) Column to 1/2 for further analysis
ScoreFinal['Sex'] = ScoreFinal['Sex'].replace('M',1)
ScoreFinal['Sex'] = ScoreFinal['Sex'].replace('F',2)

#Fill the missing score for a student to the average of the class
ScoreFinal['Score'] = ScoreFinal['Score'].fillna(ScoreFinal['Score'].mean())

#Store the data in new file – ScoreFinal.csv
ScoreFinal.to_csv('ScoreFinal.csv', index=False)

