"""
    when you open file with mode append
    if file doesn't exist python will try to create it
    if file exists --> keep old content .. start writing from
    the beginning of the file
"""

try:
    fileobject = open("mycv.txt", 'a')
except Exception as e:
    print(e)
else:
    print(fileobject)
    # fileobject.write("hiiiiii ")
    fileobject.write("hiiii\n")
    fileobject.write("Hello")
    fileobject.writelines(["hi\n", "bye\n","break\n", "boring\n"])
    # fileobject.close()