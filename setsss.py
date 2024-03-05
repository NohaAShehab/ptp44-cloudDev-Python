
"""
    no duplicates in set
    no order
    accept different datatypes
    no indices
"""

mys = {"Ahmed", "Zeinab", "iti", 3234, "Ahmed", "Mohamed", "Mohamed",
       "Mohamed", 3.12}

print(mys)


print(len(mys))


""" add element to the set ? """
mys.add("added item")
print(mys)

mys.add(("bash", "python"))
print(mys)

# mys.add(["bash", "python"]) # TypeError: unhashable type: 'list'


mys.remove("Ahmed")
print(mys)

popped_element=mys.pop()
print(mys)
print(popped_element)