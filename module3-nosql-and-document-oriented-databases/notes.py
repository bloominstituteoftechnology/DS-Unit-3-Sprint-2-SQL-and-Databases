"""function examples"""

def increment(x):
    return x + 1

def double(x):
    return x * 2

# We then imported them into python terminal to see if it worked.

def run_twice(func, arg):
    return func(func(arg))

# This isn't considered functional programming because it chnages the value of i everytime.
# It's not as safe when you're trying to scale horizontally.
# for i in range(10):
#     print(i)

# Recursion is calling the function within a function
def rec_print(n):
    print(n)
    if n >= 0:
        rec_print(n-1)

def add(x,y):
    return x + y

def identity(x):
    return x

# Now we opened map and looked at it with help(map).
# Returns function in an iterable way
# list(map(increment, [1,2,3,4])) to see the outcomes.

# from functiools import reduce

# help(reduce)

# list(map(identity, [1,2,3,4]))
# [1, 2, 3, 4]

# map_results = map(identity, [1,2,3,4])

# reduce(add, map_results)
# 10

# MangoDB uses a ton of map reduce.

# We go to MangoDB and click connect. Make a colab notebook. run !curl ipecho.net/plain
# Add an ip address from colab. Choose a connection method. Driver: python. version: 2.4 or later.
# look at full driver example.  click copy. Paste it whereever we're working. change "password" in url to your pw.
