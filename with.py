# with open('data.txt','r') as file:
#     data = file.read()

# print(data)


# with open('students.txt','w') as f:
#     f.write('Rahul Sharma,85,Bhopal\n')
#     f.write('Priya Sharma,92,Indore\n')
#     f.write('Amit Sharma,73,Jabalpur\n')


# with open('students.txt','a') as f:
#     f.write('Sneha Joshi,88,Bhopal\n')


# with open('students.txt','r') as f:
#     content = f.read()
# print(content)



# with open('students.txt','r') as f:
#     for line in f:
#         name,marks,city = line.strip().split(',')
#         print(f'{name:<15} | {marks:>5} | {city}')
#         print('-------------')



# import csv

# records = [
#     ["Name","Marks","City","Grade"],
#     ["Rahul",85,"Bhopal","B"],
#     ["Priya",92,"Indore","A"],
#     ["Amit",73,"Jabalpur","B"],
# ]
# with open('students.csv','w',newline="") as f:
#     csv.writer(f).writerows(records)



# import csv

# records = [
#     ["Name","Marks","City","Grade"],
#     ["Rahul",85,"Bhopal","B"],
#     ["Priya",92,"Indore","A"],
#     ["Amit",73,"Jabalpur","B"],
# ]
# with open('students.csv','w',newline="") as f:
#     csv.writer(f).writerows(records)
# with open('students.csv','r') as f:
#     for row in csv.DictReader(f):
#         print(f'{row['Name']}: {row['Marks']} marks ({row['City']})')





# import csv

# records = [
#     ['Name','Age','Marks','Subjects'],
#     ['Nikhil','20','97','PCM'],
#     ['Raghav','20','98','PCM'],
#     ['Mahesh','20','99','PCM'],
# ]
# with open('students.csv','w',newline='') as f:
#     csv.writer(f).writerows(records)

# name = input("Enter Students Name for Search:")

# found = False

# with open('students.csv','r') as f:
#     for row in csv.DictReader(f):
#         if row["Name"] == name:
#             print(f'Found {name}')
#         print(f'{row['Name']}: {row['Marks']} marks ({row['Subjects']})')
#         found = True
#         break

# if not found:
#     print("Students Not Found!!")




