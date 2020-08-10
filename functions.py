# Lesson 5: Functions

# Quiz: Population Density Function
# Write a function named population_density that takes two arguments, population and land_area, and returns a population density calculated from those values. 
# I've included two test cases that you can use to verify that your function works correctly. 
# Once you've written your function, use the Test Run button to test your code.

# write your function here
def population_density(population, land_area):
    density = population / land_area
    return density

# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))

# Quiz: readable_timedelta
# Write a function named readable_timedelta. 
# The function should take one argument, an integer days, and return a string that says how many weeks and days that is. 
# For example, calling the function and printing the result like this:

# write your function here
def readable_timedelta(days):
    weeks = int(days / 7)
    extra_days = int(days % 7)
    return "{} week(s) and {} day(s).".format(weeks, extra_days)

# test your function
print(readable_timedelta(10))
print(readable_timedelta(20))
print(readable_timedelta(49))


# Lambda Expressions

# Quiz: Lambda with Map
# map() is a higher-order built-in function that takes a function and iterable as inputs, and returns an iterator that applies the function to each element of the iterable. 
# The code below uses map() to find the mean of each list in numbers to create the list averages. Give it a test run to see what happens.
# Rewrite this code to be more concise by replacing the mean function with a lambda expression defined within the call to map().

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

# def mean(num_list):
#     return sum(num_list) / len(num_list)

averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)