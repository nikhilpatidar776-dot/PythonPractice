# import pandas as pd

# data = {
#     'Name':  ['Rahul','Priya','Amit','Sneha','Vikram'],
#     'Age':   [22,21,23,20,24],
#     'Marks': [85,92,78,88,73],
#     'City':  ['Bhopal','Indore','Bhopal','Jabalpur','Indore']
# } 
# df = pd.DataFrame(data)
# print(df)
# #Explore the data
# print(df.shape)
# print(df.head(3))
# print(df.dtypes)
# print(df.describe())




# import pandas as pd

# data = {
#     'Name':  ['Rahul','Priya','Amit','Sneha','Vikram'],
#     'Age':   [22,21,23,20,24],
#     'Marks': [85,92,78,88,73],
#     'City':  ['Bhopal','Indore','Bhopal','Jabalpur','Indore']
# } 
# df = pd.DataFrame(data)
# print(df)
# #Explore the data
# print(df.shape)
# print(df.head(3))
# print(df.dtypes)
# print(df.describe())

# #select columns
# print("df['Name']: \n", df['Name'])
# print(df[['Name', 'Marks']])

# # # Filter rows
# print(df[df['Marks'] >= 85])
# print(df[df['City'] >= 'Bhopal'])
# print(df[(df['Marks'] >= 80) &  (df['City'] == 'Indore')])     #multiple conditions

# def get_grade(x):
#     if x >= 90:
#         return 'A'
#     elif x >= 75:
#         return 'B'
#     else:
#         return 'C'

# df['Grade'] = df['Marks'].apply(get_grade)
# print(df['Grade'])
# print("------------")
# print(df)



# import pandas as pd

# data = {
#     'Name':  ['Rahul','Priya','Amit','Sneha','Vikram'],
#     'Age':   [22,21,23,20,24],
#     'Marks': [85,92,78,88,73],
#     'City':  ['Bhopal','Indore','Bhopal','Jabalpur','Indore']
# } 
# df = pd.DataFrame(data)
# print(df)
# # Explore the data
# print(df.shape)
# print(df.head(3))
# print(df.dtypes)
# print(df.describe())

# # GroupBy - Like Excel pivot
# city_avg = df.groupby('City')['Marks'].mean()
# print(city_avg)



import pandas as pd
import csv

data = {
    'Name':  ['Rahul','Priya','Amit','Sneha','Vikram'],
    'Age':   [22,21,23,20,24],
    'Marks': [85,92,78,88,73],
    'City':  ['Bhopal','Indore','Bhopal','Jabalpur','Indore']
} 
df = pd.DataFrame(data)
print(df)
# Explore the data
print(df.shape)
print(df.head(3))
print(df.dtypes)
print(df.describe())

# GroupBy - Like Excel pivot
city_avg = df.groupby('City')['Marks'].mean()
print(city_avg)

df.to_csv('students.csv',index=False)
df2 = pd.read_csv('students.csv')
#cleaning
df2['Name'] = df2['Name'].str.strip()
df2.to_csv('clear_output.csv', index=False)  #savedf



