

# def sumnum(num1:int, num2:int):
#     if isinstance(num1, int) and isinstance(num2,int):
#         return num1 + num2
#
#     raise TypeError("num1 and num2 must be integers")
#
#
# print(sumnum(3,4))

# print(sumnum("hello", "world"))


def divnums():
    num1 = input("please enter num1: ")
    num2 = input("please enter num2: ")
    if num2=='0':
        raise ZeroDivisionError("num2 must be zero")
    print(f"num1 = {num1}, num2={num2}")
    if num1.isdigit() and num2.isdigit():
        num1= int(num1)
        num2 = int(num2)
        res = num1/num2
        return res

divnums()





# print(int("iti"))

# print(4+"iti")