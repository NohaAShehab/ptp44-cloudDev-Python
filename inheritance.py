

# class Person:
#     pass
#
#
# class Engineer(Person): # Engineer inherits from person
#     pass
#
# eng= Engineer()
# print(isinstance(eng, Person))
#
# # all classes in python implicity inherits from class object
# print(isinstance(eng, object))


""" 2nd scenario """

# class Person:
#     def __init__(self):
#         print("I am a person")
#
#
# class Engineer(Person): # Engineer inherits from person
#     pass
#
# eng= Engineer()
# print(isinstance(eng, Person))
#
# # all classes in python implicity inherits from class object
# print(isinstance(eng, object))


"""3rd scenario"""

# class Person:
#     def __init__(self, name):
#         self.name= name
#         print("I am a person")
#
#
# class Engineer(Person): # Engineer inherits from person
#     def __init__(self, salary):
#         self.salary = salary
#         print("I am an engineer")
#
# eng= Engineer("anyvalue")
# print(isinstance(eng, Person))

"""4th scenario"""
# class Person:
#     def __init__(self, name):
#         self.name= name
#         print("I am a person")
#
#
# class Engineer(Person): # Engineer inherits from person
#     def __init__(self, name,salary):
#         # call parent constructor
#         super().__init__(name)
#         self.salary = salary
#         print("I am an engineer")
#
# eng= Engineer("anyvalue", 893712)
# print(isinstance(eng, Person))


"""5th scenario"""
# class Person:
#     def __init__(self, name):
#         self.name= name
#         print("I am a person")
#     def speak(self, message):
#         print(f"My name is {self.name}, {message}")
#
#
# class Engineer(Person): # Engineer inherits from person
#     def __init__(self, name,salary):
#         # call parent constructor
#         super().__init__(name)
#         self.salary = salary
#         print("I am an engineer")
#
#     # override
#     def speak(self,message):
#         # call speak from the parent class
#         super().speak(message)
#         print(f"My salary is {self.salary}")
#
# eng= Engineer("anyvalue", 893712)
# print(isinstance(eng, Person))
# eng.speak("Nice to meet you ")



""" multiple inheritance """


# class A:
#     def __init__(self):
#         print("A created")
#
# class B:
#     def __init__(self):
#         print("B Created")
#
#
# class Child(A, B):
#     pass
#
#
# mychild = Child()



""" diamond problem """

# class Person:
#     pass
#
# class A(Person):
#     def __init__(self):
#         print("A created")
#
# class B(Person):
#     def __init__(self):
#         print("B Created")
#
#
# class Child(A, B):
#     pass


""" 6th scenario """


# class Person:
#     def __init__(self):
#         print("I am a person")
#
# class A(Person):
#     def __init__(self):
#         print("A created")
#
# class B(Person):
#     def __init__(self):
#         print("B Created")
#
#
# class Child(A, B):
#     pass
#
#
# c= Child()





"""7th scenario"""
class Person:
    def __init__(self):
        print("I am a person")

class A(Person):
    def __init__(self):
        super().__init__()
        print("A created")

class B(Person):
    def __init__(self):
        super().__init__()
        print("B Created")


class Child(A, B):
    pass


c= Child()
print("-----")






















