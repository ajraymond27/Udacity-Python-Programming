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



 