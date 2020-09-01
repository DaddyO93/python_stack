# basic
for x in range (151):
    print(x)

# multiples of five
for x in range(0, 1001, 5):
    print(x)

# counting the dojo way
for x in range (1, 101):
    if x % 10 ==0:
        print("Coding Dojo")
    elif x % 5 ==0:
        print("Coding")
    else:
        print(x)

# Whoa. That Sucker's Huge
sum = 0
for x in range (500000):
    if x % 2 !=0:
        sum += x
print(sum)

# Countdown by Fours
for x in range(2018, 0, -4):
    if x % 2 ==0:
        print(x)

# Flexible Counter
lowNum = 0
highNum = 10
mult = 2
for x in range(highNum+1):
    if x % mult == 0:
        print(x)
        