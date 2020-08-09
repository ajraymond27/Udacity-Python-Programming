# Conditional Statements

# Practice: Which Prize
# Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored, which is stored in the integer variable points.

# Points	Prize
# 1 - 50	wooden rabbit
# 51 - 150	no prize
# 151 - 180	wafer-thin mint
# 181 - 200	penguin

# All of the lower and upper bounds here are inclusive, and points can only take on positive integer values up to 200.

# In your if statement, assign the result variable to a string holding the appropriate message based on the value of points. 
# If they've won a prize, the message should state "Congratulations! You won a [prize name]!" with the prize name. 
# If there's no prize, the message should state "Oh dear, no prize this time."

points = 174  # use this input to make your submission

if points < 1:
    result = "Oh dear, no prize this time."
elif points <= 50:
    result = 'wooden rabbit'
elif points <=150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = 'wafer-thin-mint'
elif points <= 200:
    result = 'penguin'
else:
    result = "Oh dear, no prize this time."

print('Congratulations! You won a {}!'.format(result))


# Quiz: Guess My Number
# You decide you want to play a game where you are hiding 
# a number from someone.  Store this number in a variable 
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.

answer = 27
guess = 27

if guess < answer:
    result = "Oops!  Your guess was too low."
elif guess > answer:
    result = "Oops!  Your guess was too high."
elif guess == answer:
    result = "Nice!  Your guess matched the answer!"

print(result)

# Quiz: Tax Purchase
# Depending on where an individual is from we need to tax them 
# appropriately.  The states of CA, MN, and 
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and 
# the corresponding state to assure that they are taxed by the right
# amount.

state = 'NY'
purchase_amount = 100

if state == 'CA':
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'MN':
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state == 'NY':
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)

# QUIZ: Boolean Expressions for Conditions
# Imagine an air traffic control program that tracks three variables, altitude, speed, and propulsion which for a particular airplane have the values specified below.

altitude = 10000
speed = 250
propulsion = "Propeller"

# For each of the following boolean expressions, work out whether it evaluates to True or False and match the correct value.

altitude < 1000 and speed > 100 #False
(propulsion == "Jet" or propulsion == "Turboprop") and speed < 300 and altitude > 20000 #False
not (speed > 400 and propulsion == "Propeller") #True
(altitude > 500 and speed > 100) or not propulsion == "Propeller" #True

# Quiz: Using Truth Values of Objects
# The code below is the solution to the Which Prize quiz you've seen previously. You're going to rewrite this based on what you've learned about truth values.
# You will use a new variable prize to store a prize name if one was won, and then use the truth value of this variable to compose the result message. This will involve two if statements.

# 1st conditional statement: update prize to the correct prize name based on points.
# 2nd conditional statement: set result to the correct phrase based on whether prize is evaluated as True or False.

# If prize is None, result should be set to "Oh dear, no prize this time."
# If prize contains a prize name, result should be set to "Congratulations! You won a {}!".format(prize). This will avoid having the multiple result assignments for different prizes.
# At the beginning of your code, set prize to None, as the default value.

points = 174  # use this as input for your submission

# set prize to default value of None
prize = None

# use the value of points to assign prize to the correct prize name
if points <= 50:
    prize = "wooden rabbit"
elif 151 <= points <= 180:
    prize = "wafer-thin mint"
elif points >= 181:
    prize = "penguin"

# use the truth value of prize to assign result to the correct message
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

print(result)