# class Employee2:
#     def __init__(self, name, email, salary):
#         self.name = name   # public
#         self._email = email  # protected
#         self.salary = salary
#
#     def __str__(self):
#         return f"{self.name}"  # return string
#
#     def __len__(self):
#         # return with int
#         return len(self.__dict__)
#     def __call__(self):
#         print("--- object is being called ")
# emp = Employee2("Ahmed", "ahmed@gmail.com", 5000)
# print(emp)
#
# l= [4,4,5,44]
# print(len(l))
#
# print(len(emp))
#
# emp()
#
# emp.city = 'cairo'

""" """
class Employee2:
    __slots__ = ('name',"email", 'salary', '__dict__')  # class variable
    def __init__(self, name, email, salary):
        self.name = name   # public
        self.email = email  # protected
        self.salary = salary
        self.__dict__ = {
            "name":self.name,
            "email":self.email, "salary":self.salary
        }

    def __str__(self):
        return f"{self.name}"  # return string


# emp = Employee2("Ahmed", "ahmed@gmail.com", 5000)


# emp.city = 'cairo'
# print(emp.__dict__)
############################3

## map
l = [3,5,6,23,34] # multiply items 2 ?
# mapped_list = map(lambda x:x*2, l)  # map object
# print(mapped_list)
# mapped_list = list(mapped_list)
# print(mapped_list)
# mapped_list = map(lambda x:x/2, l)
# print(mapped_list)
# mapped_list = list(mapped_list)
# print(mapped_list)
# filter
l = [3,5,6,23,34] # multiply items 2 ?
filtered_values = filter(lambda ele:ele%2==1 , l)
print(filtered_values)
filtered_values = list(filtered_values)
print(filtered_values)


# class QueueOutOfRangeException(Exception):
#     pass
#
# raise  QueueOutOfRangeException("0898098")























