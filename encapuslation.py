
"""

    limit accessibility according to specific conditions.
    access modifiers
    public
    protected
    private  ---> accessed only in the side the class

    NO ACCESS MODIFIERS IN Python!!


    use naming convention of the variables to represent access modifiers

    variable :: start[a-zA-Z] ==> public variable
    variable :: start _ ==>protected variable
    variable :: start __ ==> private variable
"""


# class Employee:
#     def __init__(self, name, email, salary):
#         self.name = name   # public
#         self._email = email  # protected
#         self.__salary = salary # private
#
#
# emp = Employee("John", "<EMAIL>",89712)
# emp.name = 'updated'
# print(emp.name)

# emp._email = 'noha@gmail.com'  # _email --> ethically don't do this

# print(emp.__salary) # AttributeError: 'Employee' object has no attribute '__salary'
# print(emp._Employee__salary) ## ethicall don't do this

""" 
    why we need encapsulation ?
    # limit accessibility --> apply condition

"""

class Employee:
    def __init__(self, name, email, salary):
        self.name = name   # public
        self._email = email  # protected
        self.__salary = salary # private

    def get_salary(self):  # return value of instance variable
        return self.__salary*.8

    def set_salary(self, salary):  # set value of instance variable
        if isinstance(salary, int ) or isinstance(salary, float) and salary >0 :
            self.__salary = salary
        else:
            raise ValueError("salary must be numeric value")


emp = Employee("Mina", "mina@gmail.com", 1000)
print(emp.get_salary())
# print(emp.set_salary("iti"))
emp.set_salary(762468)





# class Employee2:
#     def __init__(self, name, email, salary):
#         self.name = name   # public
#         self._email = email  # protected
#         if isinstance(salary, int) or isinstance(salary, float) and salary > 0:
#             self.__salary = salary
#         else:
#             raise ValueError("salary must be numeric value")
#
#     @property  # call function like property
#     def salary(self):  # return value of instance variable// property
#         return self.__salary
#
#     @property
#     def netsalary(self):
#         return self.__salary*0.7
#
#     @salary.setter
#     def salary(self, salary):  # set value of instance variable
#         if isinstance(salary, int ) or isinstance(salary, float) and salary >0 :
#             self.__salary = salary
#         else:
#             raise ValueError("salary must be numeric value")


# emp2 = Employee2("Mina", "mina@gmail.com", 1000)
#
# print(emp2.salary)
# # emp2.salary = "updated"
# emp2.salary = 10000
#
# print(emp2.netsalary)


# emp2 = Employee2("Mina", "mina@gmail.com", "iti")





class Employee2:
    def __init__(self, name, email, salary):
        self.name = name   # public
        self._email = email  # protected
        self.salary = salary

    @property  # call function like property
    def salary(self):  # return value of instance variable// property
        return self.__salary

    @property
    def netsalary(self):
        return self.__salary*0.7

    @salary.setter
    def salary(self, salary):  # set value of instance variable
        if isinstance(salary, int ) or isinstance(salary, float) and salary >0 :
            self.__salary = salary
        else:
            raise ValueError("salary must be numeric value")


emp = Employee2("Mina", "mina@fff", 7864)
emp.salary = 127867  # call setter
print("----")



print(emp._Employee2__salary)  # ethically don't do this








