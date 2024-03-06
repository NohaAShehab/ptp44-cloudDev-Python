
"""
     you can open existing files for read
"""
# try:
#     fileobject = open("students.txt", 'r')
# except Exception as e:
#     print(e)
# else:
#     print(fileobject)
#     "read content "
#     data  =fileobject.read()  # read data into one string
#     print(data)
#
#     """ move the fileobject to return it to the begining if the file"""
#     # fileobject.seek(0)  # byte number
#
#     """ read file lines """
#     # lines = fileobject.readlines()
#     # print(lines)
#     """ get file content line by line"""
#     fileobject.close()


try:
    fileobject = open("/etc/passwd", 'r')
except Exception as e:
    print(e)
else:
    print(fileobject)
    "read content "
    # data  =fileobject.read()  # read data into one string
    # print(data)
    users = fileobject.readlines()
    print(users)
    users_info = []
    for user in users:
        user = user.strip("\n")
        user_details = user.split(":")
        users_info.append(user_details)

    fileobject.close()












