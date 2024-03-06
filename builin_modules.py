
import math

# print(math.pi)
#
# print(math.sin(90))


import time
print(time.time())


import datetime

now = datetime.datetime.now()

print(now)


s2 = now.strftime("%d/%m/%Y")

print("s2:", s2)


# from datetime import datetime
# import datetime
# """ datetime"""
# datetime_str = '09/19/22'
#
# datetime_object = datetime.datetime.strptime(datetime_str, '%m/%d/%y')
# print(datetime_object)

""" os """

import os
# print(os.getcwd())
# print(os.getpid())
# os.system("ls -l")
# os.system("sudo systemctl restart apache2")
#
# os.system("clear")

import re

emailpattern= r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

email = input('Enter your email address: ')

# result = re.match(emailpattern, email)
#
# print(result)
#
# if result:
#     print('--- email valid')
# else:
#     print("--- email not valid ")
# noha@gmail.com@iti.com

# match -->return with match object if the first part of the string
# matches pattern

"fullmatch"

result = re.fullmatch(emailpattern, email)

print(result)

if result:
    print('--- email valid')
else:
    print("--- email not valid ")




















