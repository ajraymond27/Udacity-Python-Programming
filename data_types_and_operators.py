# Arithmetic operators:
# QUIZ: Average Electricity Bill
# My electricity bill for the last three months have been $23, $32 and $64. 
# What is the average monthly electricity bill over the three month period? 
# Write an expression to calculate the mean, and use print() to view the result.

print((23 + 32 + 64)/3)  

# QUIZ: Calculate
# In this quiz you're going to do some calculations for a tiler. 
# Two parts of a floor need tiling. One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 tiles long. 
# Tiles come in packages of 6.

# How many tiles are needed?
print(9*7+5*7)

# You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?
print(17*6 - (9*7 + 5*7))

# QUIZ: Which of these lines of Python code are well formatted? 
# How would you improve the readability of the codes that don't use good formatting? (Choose all that apply)
# (All below are fixed to be well formatted)

print((3 + 32) - 15//2)
print((17 - 6)%(5 + 2))
print((1 + 2 + 4)/13)
print(4/2 - 7*7)


# Variables and Assignment Operators:

# QUIZ: Assign and Modify Variables
# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall = rainfall * .9
# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall
# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume = reservoir_volume * 1.05
# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume = reservoir_volume * .95
# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5
# print the new value of the reservoir_volume variable
print(reservoir_volume)

# QUIZ: Changing Variable Values
carrots = 24
rabbits = 8
crs_per_rab = carrots/rabbits
rabbits = 12
print(crs_per_rab) #If we now add this line of code to the above, what will the output be?
# Answer: 3


# Integers and Floats

# QUIZ: int vs. float
# In the fishy situation below, some of the quantities are of type int and some are of type float. 
# Check all the ones that should be of type float.

# How many people came on your fishing trip: int
# Length of a fish you caught, in meters: float
# Number of fish caught on a fishing trip: int
# Length of time it took to catch the first fish, in hours: float

# QUIZ: Divide by zero?
# What happens if you divide by zero in Python? Try it out! Test run this code and see what happens.
#print(5/0)


# Booleans, Comparison Operators, and Logical Operators

# QUIZ: Which is denser, Rio or San Francisco
# Try comparison operators in this quiz! 
# This code calculates the population densities of Rio de Janeiro and San Francisco.
# Write code to compare these densities. Is the population of San Francisco more dense than that of Rio de Janeiro? 
# Print True if it is and False if not.

sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise

print(san_francisco_pop_density > rio_de_janeiro_pop_density)


# Strings Data Type

# QUIZ: Fix the quote
# The line of code in the following quiz will cause a SyntaxError, thanks to the misuse of quotation marks. 
# First run it with Test Run to view the error message. 
# Then resolve the problem so that the quote (from Henry Ford) is correctly assigned to the variable ford_quote.
 
 #incorrect
 #ford_quote = 'Whether you think you can, or you think you can't--you're right.'

#correct options:
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'
ford_quote = "Whether you think you can, or you think you can't--you're right."

# QUIZ
# We’ve already seen that the type of objects will affect how operators work on them.
# What will be the output of this code?
coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count)
# prints "3415"

# QUIZ: Write a Server Log Message
# In this programming quiz, you’re going to use what you’ve learned about strings to write a logging message for a server.
# You’ll be provided with example data for a user, the time of their visit and the site they accessed.
# You should use the variables provided and the techniques you’ve learned to print a log message like this one (with the username, url, and timestamp replaced with values from the appropriate variables):
# Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20.

username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TO DO print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."

print(username + " accessed the site " + url + " at " + timestamp)


# QUIZ: len()
# Use string concatenation and the len() function to find the length of a certain movie star's actual full name.
# Store that length in the name_length variable. Don't forget that there are spaces in between the different parts of a name!

given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

full_name = given_name + " " + middle_names + " " + family_name
name_length = len(full_name)

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)


# Changing Data Types

# QUIZ: Total Sales
# Calculate and print the total sales for the week from the data provided.
# Print out a string of the form "This week's total sales: xxx", where xxx will be the actual total of all the numbers.
# You’ll need to change the type of the input data in order to calculate that total.

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

# Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.

total_sales = float(mon_sales) + float(tues_sales) + float(wed_sales) + float(thurs_sales) + float(fri_sales)
print("This week's total sales:", str(total_sales))


# String Methods

# QUIZ: What happens when you call a string method like islower() on a float object? For example, 13.37.islower().
# An error occurs

# QUIZ: format() Practice
# Write two lines of code below, each assigning a value to a variable
name = "AJ Raymond"
pet = "The Bird Dogg"
# Now write a print statement using .format() to print out a sentence and the 
#   values of both of the variables
print("{} has a pet named {}".format(name, pet))
print("{} is a good boy, but technically he is Alli's {}".format(pet, "dog"))

# QUIZ: String Methods Coding Practice

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# What is the length of the string variable verse?
verse_length = len(verse)
print("The verse length is {}".format(verse_length))

# What is the index of the first occurrence of the word 'and' in verse?
occurrence = verse.find('and')
print("The word and first occurs at index {}".format(occurrence))

# What is the index of the last occurrence of the word 'you' in verse?
you_rfind = verse.rfind('you')
print("The index of the last occurrence of you is at {}".format(you_rfind))

# What is the count of occurrences of the word 'you' in the verse?
you_count = verse.count('you')
print('The word you occurs {} times in verse'.format(you_count))

