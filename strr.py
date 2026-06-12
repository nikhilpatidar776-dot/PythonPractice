# city = "Los Santos"
# print(city[0])
# print(city[2])

# print(city[-1])
# print(city[5])

# print(city[-3])
# print(city[3])




# name = "Nikhil Raj Patidar"
# print(name[0:5])
# print(name[6:])
# print(name[:5])
# print(name[::2])
# print(name[::-1])
# print(len(name))




'''upper and lower method'''
# text = 'Hello Python World'
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())
# #Strip whitestrip
# print(text.strip())
# #search
# print('Python'in text)
# print(text.find('Python'))
# print(text.count('l'))




'''replacing element in string'''
# # Split and Join
# csv = "Nikhil,22,Los santos,Engineer"
# parts = csv.split(",")
# print(parts)
# print(parts[0])
# rejoined = " | ".join(parts)
# print(rejoined)

# #check content
# print("hello123".isalnum())
# print("12345".isdigit())
# print("Python".isalpha())
# print("  ".isspace())

# #Start/end check
# email = "student@gmail.com"
# print(email.endswith(".com"))
# print(email.startswith("stu"))




# name,marks,rank = 'Nikhil',92.567,3

# #Basic
# print(f'Hello,{name}!')

# #Formate numbers
# print(f'Marks:{marks:.2f}')
# print(f'Marks:{marks:.0f}')
# print(f'Count:{1000000:,}')

# #Padding and alignment
# print(f'{name:<15}|{marks:>8.2f}|Rank:{rank}')    #left/right align
# print(f'hello{name:^10}')
# print(f'hello{name:>10}')
# print(f'hello{name:<10}')
# print(f'hello{name:*^10}')
# #Anita.           |    92.57|Rank:3


# #Expressions inside {}
# price,gst = 500,0.18
# print(f'Price:Rs.{price} | GST:Rs.{price*gst:.2f} | Total:Rs.{price*(1+gst):.2f}')




'''Question'''
string = "Hello,How are you doing today?"
#Count vowels i the string
#Print you from the string
#Print the starting in reverse order
#non_palin,palin = "abcdef",axttxa
#check if the string is palindrome or not 


string = "Hello,How are you doing today?"
count = 0
for ch in string.lower():
    if ch in "aeiou":
        count += 1 
print("Numbers of vowels:",count)

