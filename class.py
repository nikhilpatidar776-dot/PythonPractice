# class ThisIsMyFirstClass:
#     pass

# firstObject = ThisIsMyFirstClass()
# print(firstObject)





# class ThisIsMyFirstClass:
#     name = "Nikhil"
#     age = 20

#     def getName():
#         pass

# firstObject = ThisIsMyFirstClass()
# print(firstObject)





# class ThisIsMyFirstClass:
#     name = "Nikhil"
#     age = 20

#     def getName(self):
#         print(self.name)

# firstObject = ThisIsMyFirstClass()
# print(firstObject)

# firstObject.getName()





# class ThisIsMyFirstClass:
#     name = "Nikhil"
#     age = 20

#     def getName(self):
#         print(self.name)

# firstObject = ThisIsMyFirstClass()
# print(firstObject)

# firstObject.getName()
# print(firstObject.nam





# class student:
#     def __init__(self):
#         self.name = ""
#         self.age = 0
#         self.gender = ""
#         self.grade = ""

# Nikhil = student()
# print(Nikhil)

# Nikhil.name = "Nikhil Raj Patidar"
# Nikhil.age = "20"
# Nikhil.gender = "Male"
# Nikhil.grade = "12th"

# print(Nikhil.name)
# print(Nikhil.age)
# print(Nikhil.gender)
# print(Nikhil.grade)





# class student:
#     def __init__(self,name,age,gender,grade):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.grade = grade

# Nikhil = student("Nikhil Raj Patidar",20,"A","Male")
# print(Nikhil)

# print("Name:",Nikhil.name)
# print("Age:",Nikhil.age)
# print("Gender:",Nikhil.gender)
# print("Grade:",Nikhil.grade)





# class student:
#     def __init__(self,name,age,gender,grade):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.grade = grade

#     def printDetails(self):2
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Gender:", self.gender)
#         print("Grade:", self.grade)

# Nikhil = student("Nikhil Raj Patidar",20,"A","Male")
# print(Nikhil)

# Nikhil.printDetails()





# class ExampleClass:
#     counter = 0
#     def __init__(self,val = 1):
#         self.__first = val
#         ExampleClass.counter += 1

# example_object_1= ExampleClass()
# example_object_2= ExampleClass(2)
# example_object_3= ExampleClass(4)

# print(example_object_1.__dict__,example_object_1.counter)
# print(example_object_2.__dict__,example_object_2.counter)
# print(example_object_3.__dict__,example_object_3.counter)





'''class ExampleClass:
    counter = 0
    def __init__(self,val = 1):
    #self.__first = val
        ExampleClass.counter += 1
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

example_object = ExampleClass(1)
print(example_object.a)
# print(example_object.b)'''





# class ExampleClass:
#     counter = 0
#     def __init__(self,val = 1):
#         #self.__first = val
#         ExampleClass.counter += 1
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1

# example_object = ExampleClass(8)

# try:
#     print("a =",example_object.a)
# except AttributeError:
#     print("b =",example_object.b)
# except AttributeError:
#     print("The error has occured! Silently passing it!")






# class ExampleClass:
#     counter = 0
#     def __init__(self,val = 1):
#     #self.__first = val
#         ExampleClass.counter += 1
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1

# example_object = ExampleClass(6)

# if hasattr(example_object,'a'):
#     print("a =",example_object.a)

# if hasattr(example_object,'b'):
#     print("b =",example_object.b)






# class ExampleClass:
#     counter = 0
#     a = 1
#     def __init__(self,val = 1):
#     #self.__first = val
#         ExampleClass.counter += 1
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 1

# example_object = ExampleClass(6)

# if hasattr(example_object,'a'):
#     print("a =",example_object.a)

# if hasattr(example_object,'b'):
#     print("b =",example_object.b)

# print(hasattr(ExampleClass,'b'))
# print(hasattr(ExampleClass,'a'))





'''class Python:
    population = 1
    victims = 0
    def __init__(self):
        self.lenght_ft = 3
        self.__venomous = False

myObj = Python()
print("myObj.population:",myObj.population)
print("myObj.population:",myObj.victims)
print("myObj.population:",myObj.lenght_ft)
print("myObj.__venomous: ",myObj._Python__venomous)
# print("myObj.venomous: ",myObj.venomous)'''






# class Classy:
#     def visible(self):
#         print("visible")
    
#     def __hidden(self):
#         print("hidden")

# obj = Classy()
# obj.visible()
# try:
#     obj.__hidden()
# except:
#     print("failed")
# obj._Classy__hidden()






                     ##Name mangling method##


# class Classy:
#     def visible(self):
#         print("visible")
    
#     def __hidden(self):
#         print("hidden")

# obj = Classy()
# obj.visible()
# try:
#     obj.__hidden()
# except:
#     print("failed")

# obj = Classy()
# print(type(obj))
# print(type(obj).__name__)






# class Vehicle:
#     pass

# class LandVehicle(Vehicle):
#     pass

# class TrackedVehicle(LandVehicle):
#     pass

# my_vehicle = Vehicle()
# my_land_vehicle = LandVehicle()
# my_tracked_vehicle = TrackedVehicle()

# for obj in [my_vehicle,my_land_vehicle,my_tracked_vehicle]:
#     for cls in [Vehicle,LandVehicle,TrackedVehicle]:
#         print(isinstance(obj,cls),end="\t")
#         print()





# class SampleClass:
#     def __init__(self,val):
#         self.val = val

# object_1 = SampleClass(0)
# object_2 = SampleClass(2)
# object_3 = object_1
# object_3.val += 1

# print(object_1 is object_2)
# print(object_2 is object_3)
# print(object_3 is object_1)
# print(object_1.val,object_2.val,object_3.val)

# string_1 = "Marry had a little "
# string_2 = "Marry had a little lamb"
# string_1 += "lamb"

# print(string_1 == string_2,string_1 is string_2)






'''__str__method'''

# class Super:
#     def __init__(self,name):
#         self.name = name

#     def __str__(self):
#         return "My name is " + self.name + "."
    
# class Sub(Super):
#     def __init__(self,name):
#         pass
#         Super.__init__(self,name)

# obj = Sub("Nikhil")
# print(obj)




'''class Super:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."
    
class Sub(Super):
    def __init__(name):
        super().__init__(name)

obj = Sub("Nikhil")
print(obj)'''






# class SuperA:
#     var_a = 10
#     def fun_a(self):
#         return 11

# class SuperB:
#     var_b = 20
#     def fun_b(self):
#         return 21

# class Sub(SuperA,SuperB):
#     pass
# obj = Sub()
# print(obj.var_a,obj.fun_a())
# print(obj.var_b,obj.fun_b())







# class Level1:
#     var = 100
#     def fun(self):
#         return 10-1
    
# class Level2(Level1):
#     var = 200
#     def fun(self):
#         return 201
    
# class Level3(Level2):
#     pass

# obj = Level3()
# print(obj.var,obj.fun())






'''Multiple_Inheritance'''

# lass Left:
#     var = "L"
#     var_left = "LL"
#     def fun(self):
#         return "Left"
    
# class Right:
#     var = "R"
#     var_right = "RR"
#     def fun(self):
#         return "Right"
    
# class Sub(Left,Right):
#     pass

# obj = Sub()
# print(obj.var,obj.var_left,obj.var_right,obj.fun())






'''polymorphism'''

# class One:
#     def do_it(self):
#         print("do_it from One")

#     def doanything(self):
#         self.do_it()

# class Two(One):
#     def do_it(self):
#         print("do_it from Two")

# class Three(Two):
#     def do_it(self):
#         print("do_it from Two")


# one = One()
# two = Two()
# three = Three()
# one.doanything()
# two.doanything()
# three.doanything()





# class One:
#     def do_it(self):
#         print("do_it from One")

#     def doanything(self):
#         self.do_it()

# class Two(One):
#     def do_it(self):
#         print("do_it from Two")

# class Three(Two):
#     def do_it(self):
#         super().do_it()


# one = One()
# two = Two()
# three = Three()
# one.doanything()
# two.doanything()
# three.doanything()




# def reciprocal(n):
#     try:
#         n = 1/n
#     except ZeroDivisionError:
#         print("Division failed")
#         return None
#     else:
#         print("Everything went fine")
#     return n

# print("------------")
# print("reciprocal(2): ",reciprocal(2))
# print("------------")
# print("reciprocal(0): ",reciprocal(0))
# print("------------")






'''Exception class'''

# try:
#     i = int("Hello!")
# except Exception as e:
#     print(e)
#     print(e.__str__())






'''create you own exception'''

class MyZeroDivisionError(ZeroDivisionError):
    pass

def do_the_division(mine):
    if mine:
        raise MyZeroDivisionError("some worse news")
    else:
        raise ZeroDivisionError("some bad news")
    
do_the_division(False)








