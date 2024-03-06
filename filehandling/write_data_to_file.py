"""
    when you open file with mode write
    if file doesn't exist python will try to create it
    if file exists --> earse the old content
"""

try:
    fileobject = open("mycv.txt", 'w')
except Exception as e:
    print(e)
else:
    print(fileobject)
    # fileobject.write("hiiiiii ")
    fileobject.write("hiiii\n")
    fileobject.write("Hello")
    fileobject.writelines(["hi\n", "bye\n","break\n", "boring\n"])
    fileobject.close()