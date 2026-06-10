# my_tuple = (1,10,100)

# t1 = my_tuple+(1,10,100)
# t2 = my_tuple*3

# print(len(t2))
# print(t1)
# print(t2)
# print(10 in my_tuple)
# print(-10 not in my_tuple)


'''tuple_1 = (1,2,3)
for elem in tuple_1:
    print(elem)


tuple_2 = (1,2,3,4)
print( 5 in tuple_2)
print( 5 not in tuple_2)


tuple_3 = (1,2,3,4,)
print(len(tuple_3))
print(5 not in tuple_3)


tuple_4 = tuple_1 + tuple_2
tuple_5 = tuple_3 * 2
print(tuple_4)
print(tuple_5)'''



# my_tuple = tuple((1,2,"string"))
# print(my_tuple)
# print(type(my_tuple))

# my_list = [2,4,6]
# print(my_list)
# print(type(my_list))
# tup = tuple(my_list)
# print(tup)
# print(type(tup))




# var = 123


# t1 = (1,)
# t2 = (1,2)
# t3 = (1,2,3)



# dictionary = {
#     "cat":"chat",
#     "dog":"chien",
#     "horse":"cheval"
# }
# phone_numbers = {'boss':5551234567,'suzy':22657854310}
# empty_dictionary = {}

# print(dictionary)
# print(type(dictionary))
# print(phone_numbers)
# print(type(phone_numbers))
# print(empty_dictionary)
# print(type(empty_dictionary))



# dictionary = {
#     "cat":"chat",
#     "dog":"chien",
#     "horse":"cheval"
# }
# phone_numbers = {'boss':5551234567,'suzy':22657854310}
# empty_dictionary = {}

# print(dictionary)
# print(type(dictionary))
# print(phone_numbers)
# print(type(phone_numbers))
# print(empty_dictionary)
# print(type(empty_dictionary))

# print(dictionary['cat'])
# print(phone_numbers['suzy'])



# dictionary = {
#     "cat":"chat",
#     "dog":"chien",
#     "horse":"cheval"
# }
# phone_numbers = {'boss':5551234567,'suzy':22657854310}
# empty_dictionary = {}

# print(dictionary)
# print(type(dictionary))
# print(phone_numbers)
# print(type(phone_numbers))
# print(empty_dictionary)
# print(type(empty_dictionary))

# words = ['cat','lion','horse']

# for word in words:
#     if word in dictionary:
#         print(word,"->",dictionary[word])
#     else:
#         print("------",word,"is not in dictionary","------")



'''# dictionary = {
#     "cat":"chat",
#     "dog":"chien",
#     "horse":"cheval"
# }
# phone_numbers = {'boss':5551234567,'suzy':22657854310}
# empty_dictionary = {}

# print(dictionary)
# print(type(dictionary))
# print(phone_numbers)
# print(type(phone_numbers))
# print(empty_dictionary)
# print(type(empty_dictionary))

# words = ['cat','lion','horse']

# for word in words:
#     if word in dictionary:
#         print(word,"->",dictionary[word])
#     else:
#         print("------",word,"is not in dictionary","------")

# print(dictionary.keys())
# for key in dictionary.keys():
#     print(key,"->",dictionary[key])

# for key,value in dictionary.items():
#     print(key,"->",value)

# for value in dictionary.values():
#     print(value)'''


# pool_eng_dictionary = {
# "zamek":"castle",
# "woda":"water",
# "gleba":"soil"  
# }
# print("pool_eng_dictionary:",pool_eng_dictionary)
# copy_dictionary = pool_eng_dictionary.copy()

# print("copy_dictionary:",copy_dictionary)

# pool_eng_dictionary["zamek"] = "lock"
# item = pool_eng_dictionary["zamek"]
# print(item)




# phonebook = {}

# print(phonebook)
# phonebook["adam"] = 4353464576457
# print(phonebook)

# del phonebook["adam"]
# print(phonebook)




# pol_eng_dictionary = {"kwait": "flower"}

# pol_eng_dictionary.update(
#     {
#         "gleba": "soil"
#     })
# print(pol_eng_dictionary)

# pol_eng_dictionary.popitem()
# print(pol_eng_dictionary)


# pol_eng_dictionary = {
#     "zamek":"castle",
#     "woda":"water",
#     "gleba":"soil"
# }

# if "zamek1" in pol_eng_dictionary:
#     print("Yes! zamek1 is present in the Dictionary")
# else:
#     print("No! zamek is not present in the Dictionary")


# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))

# del pol_eng_dictionary["zamek"]
# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))

# pol_eng_dictionary.clear()
# print(pol_eng_dictionary)
# print(len(pol_eng_dictionary))

# del pol_eng_dictionary
# print(pol_eng_dictionary)


#           #Question#

# students_score = {}

# while True:
#     name =  input("Enter the students name:")
#     if name == "":
#         break

#     score = int(input(f"Enter {name}'s score:"))
#     if score not in range(1,11):
#         break
#     if name in students_score:
#         students_score[name] += (score,)
#     else:
#         students_score[name] = (score,)

# print(students_score)

# for name, mark in students_score.items():
#     sum = 0
#     for m in mark:
#         sum += m
#     print(name,"->",sum/len(mark))




