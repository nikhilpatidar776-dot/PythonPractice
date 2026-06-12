import pandas as pd

data = {
    'Name':  ['Rahul','Priya','Amit','Sneha','Vikram'],
    'Age':   [22,21,23,20,24],
    'Marks': [85,92,78,88,73],
    'City':  ['Bhopal','Indore','Bhopal','Jabalpur','Indore']
} 
df = pd.DataFrame(data)
print(df)
#Explore the data
print(df.shape)
print(df.head(3))
print(df.dtypes)
print(df.describe())



