"""
    functions with mandatory arguments

"""


def hello_ghaza():
    pass


"call the function "
# hello_ghaza()
# res = hello_ghaza()
# print(res)  # None

""" use keyword return """


def good_morning():
    return


# res = good_morning()
# print(res)


"""function do something"""


def notes():
    print("--It seems impossible until it is done --")


# notes()

"""function accept arugments"""


def sumnum(num1, num2):
    res = num1 + num2
    print(res)


sumnum(32, 34)

# sumnum(3,34,897)  # TypeError: sumnum() takes 2 positional arguments but 3 were given

# sumnum(7)

"""function return value """


# def mulnum(num1, num2):
#     res = num1 * num2
#     return res
#
# print(mulnum(334,5))


def mulnum(num1, num2):
    res = num1 * num2
    return num1, num2, res


# print(mulnum(334,5))

""" functions with optional arguments """

""" functions with default arguments """


def subnums(num1=7, num2=10):
    print(f"num1 = {num1}, num2={num2}")
    res = num1 - num2
    return res


# print(subnums(32,34))
# print(subnums(23))
# print(subnums())


# print()
# print("iti", end="#")
# print("Ahmed", "Mohamed", "ali", sep ="_")


""" function with variable number of arguments """

def ask_for_students(*students):  # function can accept zero or more arguments
    print(students)

#
# ask_for_students()
ask_for_students("Ahmed",
                 "Keroles")
ask_for_students("Mina", "Gehad", 876, 89797)


""" """


def introduce_your_self(**info):  # kwargs
    print(info)


introduce_your_self()
introduce_your_self(fname='noha',
            lname='shehab', work='iti')
introduce_your_self(fullname='GehadYosry', track='cloudDev')

temp = "we have {anystudents} in {anycourse}"

print(temp.format(anystudents=25, anycourse='python'))


# def ask_for_config(servicename,
#                    **config):
#     print(servicename)
#     print(config)




# def sumnum(num1, num2):
#     res = num1 + num2
#     print(res)
#
# sumnum(4,5)
# sumnum("ahmed", "Mohamed")
# sumnum("Ahmed", 10)



"""

    num1, num2 - -> integers 
    return integer 
"""

# def sumnum(num1: int, num2: int) -> int:  # documenting purpose
#     res = num1 + num2
#     print(res)
#     return res

# sumnum(4,5)
# sumnum("ahmed", "Mohamed")
# sumnum("Ahmed", 10)




def sumnum(num1: int, num2: int) -> int:  # documenting purpose
    if type(num1)== int and type(num2)== int:
        res = num1 + num2
        print(res)
        return res
    print("---- Error num1 , num2 must be integers")
    return


print(sumnum(2,34))

print(sumnum(3,"uu"))



num = 20  # object from class int

print(isinstance(num, int))


def sumnum(num1: int, num2: int) -> int:  # documenting purpose
    if isinstance(num1, int) and isinstance(num2, int):
        res = num1 + num2
        print(res)
        return res
    print("---- Error num1 , num2 must be integers")
    return


print(sumnum(2,34))

print(sumnum(3,"uu"))




