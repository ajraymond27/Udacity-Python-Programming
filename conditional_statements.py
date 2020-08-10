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
    elif key not in fruits:
        not_fruit_count += value

print(fruit_count, not_fruit_count)


# While Loops

# Practice: Factorials with While Loops
# Find the factorial of a number using a while loop.
# A factorial of a whole number is that number multiplied by every whole number between itself and 1. For example, 6 factorial (written "6!") equals 6 x 5 x 4 x 3 x 2 x 1 = 720. So 6! = 720.
# We can write a while loop to take any given number and figure out what its factorial is.
# Example: If number is 6, your code should compute and print the product, 720.

# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

# write your while loop here
while current <= number:
    # multiply the product so far by the current number
    product *= current
    
    # increment current with each iteration until it reaches number
    current += 1

# print the factorial of number
print(product)

# Practice: Factorials with For Loops
# Now use a for loop to find the factorial!
# It will now be great practice for you to try to revise the code you wrote above to find the factorial of a number, but this time, using a for loop. 

# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# write your for loop here
for i in range(1,number+1):
    product *= i
# print the factorial of number
print(product)

# Quiz: Count By
# Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num. Use break_num as the variable that you'll change each time through the loop. 
# For simplicity, assume that end_num is always larger than start_num and count_by is always positive.

# Before the loop, what do you want to set break_num equal to? 
# How do you want to change break_num each time through the loop? What condition will you use to see when it's time to stop looping?

# After the loop is done, print out break_num, showing the value that indicated it was time to stop looping. 
# It is the case that break_num should be a number that is the first number larger than end_num.

start_num = 0
end_num = 700
count_by = 7
break_num = start_num

# write a while loop that uses break_num as the ongoing number to check against end_num
while break_num < end_num:
    break_num += count_by

print(break_num)

# Quiz: Count By Check
# Suppose you want to count from some number start_num by another number count_by until you hit a final number end_num, and calculate break_num the way you did in the last quiz.

# Now in addition, address what would happen if someone gives a start_num that is greater than end_num. 
# If this is the case, set result to "Oops! Looks like your start value is greater than the end value. Please try again." 
# Otherwise, set result to the value of break_num.

start_num = 100
end_num = 50
count_by = 5
break_num = start_num

# write a condition to check that end_num is larger than start_num before looping
if end_num > start_num:
# write a while loop that uses break_num as the ongoing number to check against end_num
    while break_num < end_num:
        break_num +=count_by
        result = break_num
else:
    result = 'Oops! Looks like your start value is greater than the end value. Please try again.'

print(result)

# Quiz: Nearest Square
# Write a while loop that finds the largest square number less than an integer limit and stores it in a variable nearest_square. 
# A square number is the product of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.
# For example, if limit is 40, your code should set the nearest_square to 36.

limit = 27
square = 1

# write your while loop here
while square**2 < limit:
    nearest_square = square**2
    square += 1

print(nearest_square)

# Question: What type of loop should we use?
# You need to write a loop that takes the numbers in a given list named num_list:
# num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

# Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. If there are more than 5 odd numbers, you should stop at the fifth. 
# If there are fewer than 5 odd numbers, add all of the odd numbers.

# Would you use a while or a for loop to write this code?

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
odd_count = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while odd_count < 5 and i <= len_num_list:
    if num_list[i] % 2 == 1:
        list_sum += num_list[i]
        odd_count += 1
    i += 1

print("This function added {} odd numbers to get list_sum".format(odd_count))
print("The sum of all those odd numbers is {}".format(list_sum))
        
# Udacity's answer:
count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list): 
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print ("The numbers of odd numbers added are: {}".format(count_odd))
print ("The sum of the odd numbers added is: {}".format(list_sum))


# Break and Continue

# Try It Out!

manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# Quiz: Break the String
# Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long. 
# You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline. 
# If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.

# Remember that break works in both for and while loops. Use whichever loop seems most appropriate. 
# Consider adding print statements to your code to help you resolve bugs.

# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)

# Coding Quiz: Check for Prime Numbers
# Prime numbers are whole numbers that have only two factors: 1 and the number itself. The first few prime numbers are 2, 3, 5, 7.
# For instance, 6 has four factors: 1, 2, 3, 6.
# 1 X 6 = 6
# 2 X 3 = 6
# So we know 6 is not a prime number.
# In the following coding environment, write code to check if the numbers provided in the list check_prime are prime numbers.
# If the numbers are prime, the code should print "[number] is a prime number."
# If the number is NOT a prime number, it should print "[number] is not a prime number", and a factor of that number, other than 1 and the number itself: "[factor] is a factor of [number]".

## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor


