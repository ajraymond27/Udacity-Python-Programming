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


# For Loops

# Practice: Quick Brown Fox
# Use a for loop to take a list and print each element of the list in its own line.
sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

for word in sentence:
    print(word)

# Practice: Multiples of 5
# Write a for loop below that will print out every whole number that is a multiple of 5 and less than or equal to 30.
for i in range(5, 35, 5):
    print(i)

# Quiz: Create Usernames
# Write a for loop that iterates over the names list to create a usernames list. 
# To create a username for each name, make everything lowercase and replace spaces with underscores. 
# Running your for loop over the list:

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    usernames.append(name.lower().replace(" ", "_"))
print(usernames)

# Let's say instead of creating a new list, we want to modify the names list itself with the changes and write the following code. What would this do?
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

for name in names:
    name = name.lower().replace(" ", "_")

print(names)
# It prints the original list. Must use range() to change the list itself - otherwise the changes must be assigned to a new variable

# Quiz: Modify Usernames with Range
# Write a for loop that uses range() to iterate over the positions in usernames to modify the list. 
# Like you did in the previous quiz, change each name to be lowercase and replace spaces with underscores.

usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for index in range(len(usernames)):
    usernames[index] = usernames[index].lower().replace(" ", "_")

print(usernames)

# Quiz: Tag Counter
# Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. XML is a data language similar to HTML. 
# You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". 
# Keep track of the number of tags using the variable count.
# You can assume that the list of strings will not contain empty strings.

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)

# Quiz: Create an HTML List
# Write some code, including a for loop, that iterates over a list of strings and creates a single string, html_str, which is an HTML list. 
# For example, if the list is items = ['first string', 'second string'], printing html_str should output:
# <ul>
# <li>first string</li>
# <li>second string</li>
# </ul>
# That is, the string's first line should be the opening tag <ul>. 
# Following that is one line per element in the source list, surrounded by <li> and </li> tags. The final line of the string should be the closing tag </ul>.

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>"

print(html_str)

# QUIZ:
# If you want to create a new list called lower_colors, where each color in colors is lower cased, which code line should be inserted into the code block below?
colors = ['Red', 'Blue', 'Green', 'Purple']
lower_colors = [ ]

for color in colors:
    #finish this part
    lower_colors.append(color.lower())

print(lower_colors)


# Building Dictionaries
# Method 1: Using a for loop to create a set of counters
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1
print(word_counter)

# Method 2: Using the get method
book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1
print(word_counter)

# Iterating Through Dictionaries with For Loops

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }
# only prints keys
for key in cast:
    print(key)

# If you wish to iterate through both keys and values, you can use the built-in method items like this:
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))

# Quiz: Fruit Basket - Task 1
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of fruits. 
# Use the dictionary and list to count the total number of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for key, value in basket_items.items():
#if the key is in the list of fruits, add the value (number of fruits) to result
    if key in fruits:
        result += value
print(result)

# Quiz: Fruit Basket - Task 2
# If your solution is robust, you should be able to use it with any dictionary of items to count the number of fruits in the basket. 
# Try the loop for each of the dictionaries below to make sure it always works.

#Example 1

result = 0
basket_items = {'pears': 5, 'grapes': 19, 'kites': 3, 'sandwiches': 8, 'bananas': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for key, value in basket_items.items():
    if key in fruits:
        result += value

print(result)

#Example 2

result = 0
basket_items = {'peaches': 5, 'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for key, value in basket_items.items():
    if key in fruits:
        result += value

print(result)


#Example 3

result = 0
basket_items = {'lettuce': 2, 'kites': 3, 'sandwiches': 8, 'pears': 4, 'bears': 10}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# Your previous solution here
for key, value in basket_items.items():
    if key in fruits:
        result += value

print(result)

# Quiz: Fruit Basket - Task 3
# So, a couple of things about the above examples:

# It is a bit annoying having to copy and paste all the code to each spot - wouldn't it be nice to have a way to repeat the process without copying all the code? Don't worry! 
# You will learn how to do this in the next lesson!

# It would be nice to keep track of both the number of fruits and other items in the basket.

# Use the environment below to try out this second part.
fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for key, value in basket_items.items():
#if the key is in the list of fruits, add to fruit_count.
    if key in fruits:
        fruit_count += value
#if the key is not in the list, then add to the not_fruit_count
    else key not in fruits:
        not_fruit_count += value

print(fruit_count, not_fruit_count)
