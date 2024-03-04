
name = 'ahmed'
Name = 'mohamed'

if name== 'ahmed':
    print("Hello ahmed!")


# bio= ("My name is Noha"
#       "I works at ITI "
#       "I lives in cairo")
#
# print(bio)


# this is a comment in python


bio= ("My name is Noha\n"
      "I works at ITI\n"
      "I lives in cairo")

print(bio)

# python provides multi-line string

bio2 = '''My name is Noha
I works at ITI
I lives in cairo'''
print(bio2)

paragraph ="""
sdkjkf
ajfh
kaf
"""

"""this is considered to be a comment """

'this is another comment '

age = 31
"""
    int age = 31 ; 
    
    age = 434
    
    age = "iti" // compilation error
"""
print(type(age))
age = "iti"
print(type(age))

"""****** conversion between types in python ***************"""
# year = 2024
#
# "cast numberto string "
# print(type(year))
# year = str(year)
# print(type(year))

""" cast number to float """
num = 10
print(type(num))
num = float(num)
print(type(num))

"""cast value to boolean """
name = 'ahmed'
name = bool(name)

"""cast string to int """
grade = "100"
grade = int(grade)
print(grade, type(grade))

# name = 'noha'
# name = int(name) # ValueError: invalid literal for int() with base 10: 'noha'

# name = "100Ahmed" # ValueError: invalid literal for int() with base 10: '100Ahmed'
# name = int(name)
# print(name, type(name))


""" logical operators """
print(10 and "iti")  # iti ===> represent True

print("iti" and "abc" and 100000 and -10000000000)  # -1000000--> represent True


print(bool("jkhjkh"))

print(bool(""))


print(bool("                               "))

name= "                                                           "


if name == 'ahmed':
    print("-- hello world ")
elif name =='mohamed':
    print("----- bye")
else:
    print("000000000000")