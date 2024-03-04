
num = 0
newll = []
while num < 10:
    newll.append(num)
    num +=1

print(newll)

# range

# myr = range(0 , 10 )
# print(myr)
#
# print(list(myr))

myr = range(0 , 10, 2 )
print(myr)

print(list(myr))


myrange = range(10 , 1 , -1)
print(list(myrange))

for item in myrange:
    print(item)

"ahmed ==> hmd"

"""
 3 
    1     2            3 
    1*1   1*2  2*2   3*1 3*2 3*3
 [ [1] , [2,4] , [3,6,9]]


"""

"""
    Don't ever trust user input 
    input ===> ---> as number ---> 
    check input --> can be converted to string 
"""

