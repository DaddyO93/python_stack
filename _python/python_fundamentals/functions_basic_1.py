#1
def a():
    return 5
print(a())

# Predicted outcome - 5

# Outcome - 5

#2
def a():
    return 5
print(a()+a())

# Predicted Outcome - 10

# Outcome - 10

#3
def a():
    return 5
    return 10
print(a())

# Predicted Outcome - 5

# Outcome - 5

#4
def a():
    return 5
    print(10)
print(a())

# Predicted Outcome - 5

# Outcome - 5

#5
def a():
    print(5)
x = a()
print(x)

# Predicted Outcome - (incorrect bc a() didn't return anything)
# 5
# 5

# Outcome - 
# 5
# none

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

# Predicted Outcome - (The first a() printed bc it passed two arguments, but an error occured bc we tried to add two noneTypes together)
# none

# Outcome - 
# 3
# 5Traceback (most recent call last):
#   File "c:\Users\Stand\Documents\GitHub\Coding-Dojo-Files\python_extra_files\tempCodeRunnerFile.py", line 3, in <module>
#     print(a(1,2) + a(2,3))
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

# Predicted Outcome - 
# 25

# Outcome -
# 25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

# Predicted Outcome - (incorrect bc function exits on Return)
# 100
# 7

# Outcome - 
# 100
# 10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

# Predicted Output - 
# 7
# 14
# 21

#Output - 
# 7
# 14
# 21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))

# Predicted Output - 
# 8

# Output - 
# 8

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

# Predicted Output - (incorrect bc a() did not return the new value for b - b was still set at 500)
# 500
# 500
# 300
# 300

# Output - 
# 500
# 500
# 300
# 500

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

# Predicted Output - (incorrect bc a() had a returned value of 300, b was not changed to 300 outside of the function)
# 500
# 500
# 300
# 300

# Output - 
# 500
# 500
# 300
# 500

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

# Predicted Output - 
# 500
# 500
# 300
# 300

# Output - 
# 500
# 500
# 300
# 300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

# Predicted Output - 
# 1
# 3
# 2

# Output - 
# 1
# 3
# 2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

# Predicted Output - 
# 1
# 3
# 5
# 10

# Output
# 1
# 3
# 5
# 10