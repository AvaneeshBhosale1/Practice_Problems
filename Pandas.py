#Creating Series from List
import pandas as pd

a = [1,7,2]

myvar = pd.Series(a)
print(myvar)


#Assiging labels 
import pandas as pd

a = [1,7,2]

myvar = pd.Series(a, index = ["x","y","z"])
print(myvar)


#naming the series

import pandas as pd
s1 = pd.Series([10,20,30], index = ["x","y","z"], name ='Example series')
print(s1)


#Creating Series from Dictionary
import pandas as pd
s2=pd.Series({'x':1,'y':2,'z':3})
print(s2)
#OR
s2=({'x':1,'y':2,'z':3})
myvar = pd.Series(s2)
print(myvar)



#Dataframe

import pandas as pd

data = {
    "calories": [420,380,390],
    "duration": [50,40,45]
}

print(pd.DataFrame(data))


#Locate Row

import pandas as pd

data = {
       "calories": [420,380,390],
       "duration": [50,40,45] 
}

df = pd.DataFrame(data)
print(df.loc[0])
print(df.loc[[0,1]])


#Named Indices

import pandas as pd

data = {
       "calories": [420,380,390],
       "duration": [50,40,45] 
}

df = pd.DataFrame(data, index=["day1","day2","day3"])
print(df)


#Data Cleaning
import pandas as pd

data = {
    'A': [1,2,3,None,5],
    'B': [None,2,3,4,5],
    'C': [1,2,None,None,5]
}

df = pd.DataFrame(data)
print("Original data:\n",df)

df_cleaned = df.dropna()#deletes rows with missing values
print("Cleaned data:\n", df_cleaned)


#Filling Missing Values with 0

import pandas as pd

data = {
    'A': [1,2,3,None,5],
    'B': [None,2,3,4,5],
    'C': [1,2,None,None,5]
}

df = pd.DataFrame(data)
print("Original data:\n",df)

df.fillna(0, inplace = True)
print(df)


#Filling Missing Values with other values(here, the mean of the other values in the column)

import pandas as pd

data = {
    'A': [1,2,3,None,5],
    'B': [None,2,3,4,5],
    'C': [1,2,None,None,5]
}

df = pd.DataFrame(data)
print("Original data:\n",df)

df.fillna(df.mean(), inplace = True)
print(df)


