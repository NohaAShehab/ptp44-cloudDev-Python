

def sumnum(num1, num2):
    res = num1* num2
    print(res)


# sumnum(2,2)
# sumnum(2,4)


print("------------------------------")
# print(iti)

# num = int(input("please enter number : "))

# print(3/0)



# try:
#     num = int(input("please enter number "))
# except :
#     print("error happened ")


""" define exception type """
# try:
#     num = int(input("please enter number "))
#     res = 6/ num
# except Exception as e :
#     print(f"error happened  : {e}")


"""specify action for each exception type"""
#
# try:
#     num = int(input("please enter number "))
#     res = 6/ num
#     l = []
#     l[0] = "iti"
# except ValueError as ve :
#     print(f"error happened  : {ve}")
#     print("--- num must be integer value ")
# except ZeroDivisionError as ze:
#     print(f"{ze}: you are dividing by zero which is not allowed ")
# except Exception as e:
#     print(f"---- error please restart the program {e}")
#     exit()


# l = [4,5]
# l[100]="noha"

"""----> check this """

# try:
#     num = int(input("please enter number"))
# except Exception as e:
#     print(e)
#
# else:
#     """ this block will be executed if the try executed successfully"""
#     print(num*10)

""" finally """


# try:
#     num = int(input("please enter number"))
# except Exception as e:
#     print(e)
#
# else:
#     """ this block will be executed if the try executed successfully"""
#     print(num*10)
#
# finally:
#     print("--- this block will be executed always ")
#
# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

""" when you use try except in the function """
def askforInt():
    try:
        num = int(input("please enter number"))
    except Exception as e:
        print(e)
        return False

    else:
        """ this block will be executed if the try executed successfully"""
        print(num * 10)
        return num

    finally:
        """ execution of finally block preceeds the return """
        print("--- this block will be executed always ")

    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")




print(askforInt())







