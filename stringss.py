""" define string """
work = "information technology institute"

"1- get len of the string "
print(len(work))

"2- slicing string "
print(work[2:5])
print(work[6:])
print(work[::])
print(work[::-1])  # reverse the string
print(work[::2])

"""count char occurence in string """

print(work.count("i"))

""" access char at index """
print(work[10])

"""get index of char"""

print(work.index("i"))  # return with first occurrence of the string

""" 
string is immutable datatype ?

"""
""" convert string --> upper lower // title // capitalize """

name = 'ahmed mohamed'
print(name.upper())  # return new string --> in upper cases
print(name.lower())
print(name.title())
print(name.capitalize())


""" string concat"""
message = 'hello'
message2 = 'Ghaza'
year = 2024
message3 = message + message2
print(message3)

# message4 =  message + message2 + year  # TypeError: can only concatenate str (not "int") to str


"""format string """
no_of_students = 25
course = "python"
info = "we have {0} student in {1} course"  # temp --> later --> format string
print(info)
print(info.format(no_of_students, course))  # format return new string
print(info.format(20 , "mongo"))
print(info.format(course, no_of_students))

""" define template"""
info = "we have {studentsnumber} student in {coursename} course"
print(info)
# format using keyword argument
print(info.format(coursename='mongo', studentsnumber='25'))

""" f-format string  ---> format string based on existing variables in memory"""
fname = 'noha'
midname = 'Abdelhady'
lname=  'shehab'

fullname = f"{fname} {midname} {lname}"
print(fullname)

""" interpolation"""
fullname = fname +" "+ midname *2  +" "+ lname
print(fullname)


""" loop over the string """
name = 'noha'
for abbass in name:
    print(f"char: {abbass}")

"check if char exists in string"
print("n" in name)

""" strip string """
message = "      Hello world           "
print(len(message))
print(message)
"remove spaces in one line -from the beginning of the string -"
print(message.strip()) # remove white spaces from begining and the end of the string
print(message.lstrip())
print(message.rstrip())

""" strip specific chars from string """

message= "   @ hello world @    @"
print(message.strip("@"))  # strip @ from beginning and end of the string
print(message.strip(" @do"))

"remove char from inside the string ? "
message ="hello world o o o o o "
print(message.replace("o", ""))
print(message.replace("o", "@"))
print(message.replace("o", "@", 1))

""" ask use to enter string """
# name = input("please enter your name : ")  # input returns with string
# print(name , type(name))

""" ===> calculator """

num1 = input("please enter first number")  # string
num2=  input("please enter second number") # string
res = num1 + num2  # concat
# print(res)
# res = int(num1) + int(num2)
# print(res)

""" examine string content before ---. """
print("isdigit:", num1.isdigit())  # return true if string consists only from number 0-->9
print("is alpha:", num2.isalpha())  # return True if string consists only from alphas a-zA-Z
print("isupper: ",num1.isupper())
print("islower: ",num2.islower())


name = "any string"
name +="iti"  # create new string
print(name)