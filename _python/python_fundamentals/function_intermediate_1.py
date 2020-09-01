import random
def randInt(min=0, max=100):
    num = random.random()*max
    return round(num)

print(randInt()) 		# should print a random integer between 0 to 100


import random
def randInt(min=0, max=100):
    num = random.random()*max
    return round(num)

print(randInt(max=50)) 	# should print a random integer between 0 to 50


import random
def randInt(min=0, max=100):
    num = random.random()*(max-min)+min
    return round(num)

print(randInt(min=50)) 	# should print a random integer between 50 to 100


import random
def randInt(min=0, max=100):
    num = random.random()*(max-min)+min
    return round(num)

print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
