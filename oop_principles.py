
"""

    OOP programming paradigm --> used to generate architecture can be used later
        --> all objects from the same class have the same properties and can do
        the same functionality
        --> apply oop principles
"""

# emp1 = {
#     "first_name": "Ahmed",
#     "last_name": "Ali",
#     "salary":1000,
#     "age":25
# }
#
# emp2 = {
#     "fname": "Mohamed",
#     "lname": "Hassan",
#     "emp_salary":3000,
#     "age":25
# }


# def printEmpInfo(emp):
#     print(emp["first_name"], emp["last_name"], emp["salary"], emp["age"])
#
#
# printEmpInfo(emp1)
# printEmpInfo(emp2)


""" 
    define our own datatype --> 
    --> custom properties 
    --> custom functionality
    
    create classes! 
"""
# l = []
# res = type(l) # <class 'list'>
# print(res)
# print(type(res))  # <class 'type'>


""" define the class """
# class Employee:
#     pass
#
""" take an object from class"""
# emp = Employee()
# print(type(emp))
# res2=type(emp)
# print(type(res2))

""" what happened when you create a class and take an object ?"""

# class Employee:
#     pass
#
# emp = Employee()
# print(emp)
#
# # loosely dynamically typed lang. --> add properties in the runtime
# emp.name = 'Ahmed'
# emp.salary = 1000
#
#
# emp2= Employee()
# emp2.fname= 'Ahmed'
# emp2.lastname = 'Ahmed'
# emp2.email = '<EMAIL>'



""" customize object creation """

# class Employee:
#     def __init__(self):
#         """ when create object __init__ is called, --> provide object address
#         self --> represent object address in memory
#         """
#         print(f"--{self}\nthis function is being called while creating the object\n\n")
#
# emp = Employee()
# print("emp1 -> ",emp)
#
# emp2= Employee()


"""2nd scenario"""

# class Employee:
#     def __init__(self):
#         self.name = 'Ahmed'
#         self.salary = 10000
#         self.email = '<EMAIL>'
#
#
# emp = Employee()
# print("emp1 -> ",emp)
#
# emp2= Employee()



"""3rd scenario"""
# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name
#         self.salary = salary
#         self.email = email


# emp = Employee("Ahmed", "ahmed@gmail.com", 87896)
# print("emp1 -> ",emp)
#
# emp2= Employee("Ali", "ali@gmail.com", 7678564)



"""4th scenario"""

# class Employee:
#     def __init__(self, name="", email="", salary=""):
#         """ name , salary , email instance variables
#         their values depends on caller instance """
#         self.name = name
#         self.salary = salary
#         self.email = email
#
# emp= Employee()
# print(emp.salary)
#
# emp2 =Employee("Ahmed", "ahmed@gmail.com", 87454)
# print(emp2.salary)
#



""" multiple constructors ??? """

# class Employee:
#
#     def __init__(self, name):
#         self.name = name
#     def __init__(self, name, email, salary):
#         """ name , salary , email instance variables
#         their values depends on caller instance """
#         self.name = name
#         self.salary = salary
#         self.email = email
#
# emp= Employee("Noha")


""" object properties ,,, can do functionality """

# class Employee:
#     def __init__(self, name, email, salary):
#         self.name =name
#         self.email =email
#         self.salary = salary
#
#     """ instance method --> the first parameter //represent instance
#         self
#     """
#     # define behaviour in the class
#     def printEmployee(self):
#         print(f"name={self.name}, email={self.email}, salary={self.salary}")


# emp1 = Employee("John", "<EMAIL>",73131)
# emp1.printEmployee()
#
# emp2 = Employee("test", "test", "test")
# emp2.printEmployee()






""" define property in the class represents no of objects taken from class """
# class Employee:
#     """ class variable --> its value represent class property -->
#     doesn't depend on instances"""
#     count = 0  # class variable
#     def __init__(self, name, email, salary):
#         self.name =name
#         self.email =email
#         self.salary = salary
#         #
#
#
#
# print(Employee.count)  # call class variable using className
# Employee.count +=10
#
# emp=Employee("John","<EMAIL>",2233)
# emp2= Employee("John","<EMAIL>", 781236)
# ## display object properties --> inform of dict
# print(emp.__dict__)


"""2nd scenario"""
""" class variable shared property between all instances from the class """
class Employee:
    count = 0  # class variable
    def __init__(self, name, email, salary):
        self.name =name
        self.email =email
        self.salary = salary
        # Employee.count +=1
        self.__class__.count +=1



print(Employee.count)  # call class variable using className


emp=Employee("John","<EMAIL>",2233)
print(Employee.count)  # call class variable using className
emp2= Employee("John","<EMAIL>", 781236)
print(emp.__dict__)
print(Employee.count)  # call class variable using className














































