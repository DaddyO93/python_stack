# Countdown
x = 5
numList = []
def count_down(x):
    for i in range (x, -1, -1):
        numList.append(i)
    return numList

count_down(x)
print(numList)

# Print and ruturn
a=1
b=2
def nums(a,b):
    print(a)
    return b

print(nums(a,b))

# First Plus Length 
numList = [1,2,3,4,5]
def first_last(numList):
    x=numList[0]
    y=len(numList)
    return x+y

print(first_last(numList))

# Values Greater than Second
numList = [1,2,3,4,5]
newList = []
def greater_second (numList):
    temp = 0
    for i in numList:
        if i>numList[1]:
            newList.append(i)
            temp +=1
    print(temp)
    if temp<2:
        return False
    else:
        return newList
    
print(greater_second(numList))

# This Length, That Value
a=5
b=4
newList = []
def length_value (a,b):
    for i in range(a):
        newList.append(b)
    return newList

print(length_value(a,b))
