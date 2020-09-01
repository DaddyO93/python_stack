# 1. TASK: print "Hello World"
print( "Hello World" )

# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
other_name = "Russ"
another_name = "Russ"
print( "Hello", other_name )	# with a comma
print( "Hello " + another_name)	# with a +

# 3. print "Hello 42!" with the number in a variable
name = 42
num = 7
another_num = 5
print( "Hello", num, "!" )	# with a comma
print( "Hello " + str(another_num) + "!" )	# with a +	-- this one should give us an error!

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
fave_food3 = "BBQ chicken"
fave_food4 = "fish"
fave_food5 = "fruit"
fave_food6 = "pizza"
print( "I love to eat {} and {}.".format(fave_food3, fave_food4) ) # with .format()
print( f"I love to eat {fave_food5} and {fave_food6}." ) # with an f string
