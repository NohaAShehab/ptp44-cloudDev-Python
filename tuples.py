
""" tuple is the most common datatype in python
    tuple is immutable datatype ---> cannot be changed after creation

"""

"1- define a tuple "
t = ()
myt = tuple()
#
#
"tuple can hold different data from different datatypes"
myt = (34,4, "iti", 344.32, ("ahmed", True), ['kubernates', 'GCP', "ansible"], "iti")
#
""" each element is assigned to an index --> index start from 0 """
print(myt[4])
print(myt[5][2])
#
"get len of tuple"
print(len(myt))
#
"count element occurence"
print(myt.count("iti"))
#
"""get index of element """
print(myt.index("iti"))  # get index of the first occurence
#
"""slicing the tuple"""
print(myt[3:5])  # return new tuple
print(myt[::2])
#
# """tuple is immutable datatype --> can be changed after creation"""
# """modify existing element"""
# print(myt)
# myt[1] = "updated" # TypeError: 'tuple' object does not support item assignment

# print(myt)
#

#
#




#

#

#
#
""" loop over the tuple """

for element in myt:
    print(f"element = {element}")

#
"""check element in tuple or not """
print("iti" in myt)
#
#
"""---> tuple concat"""
l1 = ("python", "mongo", "javascript", "sql")
l2= ("jenkins", "GCP", "Ansible", "Kubernates", "Docker")
lst_of_courses = l1  + l2
print(lst_of_courses)
#


# """ casting string to a tuple """
name = 'noha'
name = tuple(name)
print(name)


#
#
print(min((3,454,23,323,12,21)))
print(max((3,454,23,323,12,21)))
index  = 0

#
#
myt_enum = enumerate(myt)
print(myt_enum)
#
valuesss = tuple(myt_enum)
print(valuesss)
# # for i , value in myt_enum:
# #     print(f"i={i}, item = {value}")


"tuple of one item ? "
students = ("sara_asmaa",)