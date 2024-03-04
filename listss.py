
""" list is the most common datatype in python
    list is mutable datatype ---> can be changed after creation

"""

"1- define a list "
l = []
myl = list()


"list can hold different data from different datatypes"
myl = [34,4, "iti", 344.32, "ahmed", True, ['kubernates', 'GCP', "ansible"], "iti"]

""" each element is assigned to an index --> index start from 0 """
print(myl[4])
print(myl[6][2])

"get len of list"
print(len(myl))

"count element occurence"
print(myl.count("iti"))

"""get index of element """
print(myl.index("iti"))  # get index of the first occurence

"""slicing the list"""
print(myl[3:5])  # return new list
print(myl[::2])

"""list is mutable datatype --> can be changed after creation"""
"""modify existing element"""
print(myl)
myl[1] = "updated" # at existing index
print(myl)

# myl[100]='new value'  # IndexError: list assignment index out of range
# print(myl)


""" add element to the list """
myl.append("new element") # add element at the end of the list

"insert in certain position"
myl.insert(2, "inserted element")

myl.insert(100 , "anyvalue")  # at the end

""" remove element from list """
print(myl)
popped_value=myl.pop()  # remove element from the end of the list
print(popped_value)
print(myl)

"""remove element at index --> """
popped_index_value=myl.pop(4)
print(popped_index_value)
print(myl)

"""remove element from the list"""
myl.remove("iti")
print(myl)


""" loop over the list """

for element in myl:
    print(f"element = {element}")


"""check element in list or not """
print("iti" in myl)


"""---> list concat"""
l1 = ["python", "mongo", "javascript", "sql"]
l2= ["jenkins", "GCP", "Ansible", "Kubernates", "Docker"]
lst_of_courses = l1  + l2
print(lst_of_courses)

"""extend a list """
l1.extend(l2)
print(l1)
print(l2)

""" sort list --> comparing  ---> list --> elements from the same type """
# print("iti" > 10) # TypeError: '>' not supported between instances of 'str' and 'int'
print(lst_of_courses)
lst_of_courses.sort()  # sort in the same object
print(lst_of_courses)

lst_of_courses.sort(reverse=True)
print(lst_of_courses)

""" reverse the list ? """

myl.reverse()
print(myl)

""" casting string to a list """
name = 'noha'
name = list(name)
print(name)

"""split string to a list """
message = 'we support ghaza'
newl = message.split("a")
print(newl)


print(min([3,454,23,323,12,21]))
print(max([3,454,23,323,12,21]))
myl.append("iti")
index  = 0
for item in myl:
    print(f" {item} , {myl.index(item)} : {index}")
    index +=1


myl_enum = enumerate(myl)
print(myl_enum)

valuesss = list(myl_enum)
print(valuesss)
# for i , value in myl_enum:
#     print(f"i={i}, item = {value}")