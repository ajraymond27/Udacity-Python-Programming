# Lists

# QUIZ: List Indexing
# Use list indexing to determine how many days are in a particular month based on the integer variable month, and store that value in the integer variable num_days. 
# For example, if month is 8, num_days should be set to 31, since the eighth month, August, has 31 days.
# Remember to account for zero-based indexing!

month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month
num_days = days_in_month[month-1]

print(num_days)

# QUIZ: Slicing Lists
# Select the three most recent dates from this list using list slicing notation. Hint: negative indexes work in slices!
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])


#List Methods

# QUIZ: len, max, min, and Lists
# What would the output of the following code be? 
a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)])) # 4
print(min([len(a), len(b), len(c)])) # 2

# QUIZ: sorted, join, and Lists
# What would the output of the following code be?
names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names))) # Albert & Ben & Carol & Donna

# QUIZ: append and Lists
# What would the output of the following code be?
names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names)) # ["Carol", "Albert", "Ben", "Donna", "Eugenia"]


# Tuples 

# QUIZ: Tuples
# What would the output of the following code be? 
tuple_a = 1, 2
tuple_b = (1, 2)

print(tuple_a == tuple_b) #true
print(tuple_a[1]) # 2


# Sets

# QUIZ: list to set
# What would the output of the following code be?
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(b)
print(len(a) - len(b)) # 6

# QUIZ: add and pop
# After executing this code, will the number 5 be a part of the set b?
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
b.pop() # maybe


# Dictionaries

# QUIZ: Define a Dictionary
# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {"Shanghai": 17.8, "Istanbul": 13.3, "Karachi": 13.0, "Mumbai": 12.5}
print(population)


# QUIZ: 
# What will the output of the following code be? (Treat the commas in the multiple choice answers as newlines.)
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)

# QUIZ: 
# Use the dictionary below to answer ALL of the questions regarding dictionaries. Consider you have a dictionary named animals that looks like this:

animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3,4,2,8,2,4], 'rabbits': [2, 3, 3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}
print(animals['dogs'])
print(animals['dogs'][3])
# print(animals[3])

# Quiz: Adding Values to Nested Dictionaries
# Try your hand at working with nested dictionaries. Add another entry, 'is_noble_gas,' to each dictionary in the elements dictionary. 
# After inserting the new entries you should be able to perform these lookups:
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't

elements['hydrogen']['is_noble_gas'] = "no"
elements['helium']['is_noble_gas'] = "yes"

print(elements)


# Practice Questions

# Quiz: Count Unique Words
# Your task for this quiz is to find the number of unique words in the text. In the code editor below, complete these three steps to get your answer.
# Split verse into a list of words. Hint: You can use a string method you learned in the previous lesson.
# Convert the list into a data structure that would keep only the unique elements from the list.
# Print the length of the container.

verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, '\n')

# split verse into list of words
verse_list = verse.split()
print(verse_list, '\n')

# convert list to a data structure that stores unique elements
verse_set = set(verse_list)
print(verse_set, '\n')

# print the number of unique words
num_unique = len(verse_set)
print(num_unique, '\n')


# Quiz: Verse Dictionary
# In the code editor below, you'll find a dictionary containing the unique words of verse stored as keys and the number of times they appear in verse stored as values. 
# Use this dictionary to answer the following questions. Submit these answers in the quiz below the code editor.
verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(verse_dict)
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = verse_dict.get('breathe')
print(contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(sorted_keys[-1]) 


