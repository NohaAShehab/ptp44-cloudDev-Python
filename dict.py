
info = ["noha", 31, "iti"]  # unlabeled data

"""
    dict  ===> non primitive data ==> data ---> comma seperated key:value
    {K:V}
"""

"""1- define dict """
d = {} # dict
myd = dict()


"""2- dict can hold different data from different datatypes
dict doesn't allow key duplication
"""
info = {
    "name":"noha",
    "age":31,
    "track":"cloud",
    "courses": ["python","bash","linux"],
    "name":"Noha Shehab"
}

print(info)


""" access elements using key """
print(info["age"])
""" dict is mutable datatype """
info["age"] = 32
print(info)
info["city"] = 'Giza'  # if key doesn't exist ==> will add it
print(info)


"get len of dict "
print(len(info))

"""check if value exists in dict """
print("Giza" in info)

""" get keys"""
info_keys = info.keys()  # dict_keys
print(info_keys)
keys = list(info_keys)
"""get values ?"""
info_values = info.values()  # dict_values
print(info_values)
vals = list(info_values)
print("Giza" in info.values())


"""loop over the dict """
for abbass in info:
    print(f"{abbass}")


for abbass in info:
    print(f"{abbass}: {info[abbass]}")


""""""
# for k , v in info: # ValueError: too many values to unpack (expected 2)
#     print(f"{k}, {v}")

for k , v in info.items():
    print(f"{k}: {v}")


"""concat dict """
basic_info = {"fname": "Mohamed", "lname":"thrwat", "age":23, "uni":"AinShams"}
salary_ref = {"salary":"100" , "currency":"KWD"}

# m_info = basic_info + salary_ref #TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# print(m_info)

basic_info.update(salary_ref)
print(basic_info)

"""remove value from dict """
basic_info.pop("fname")




