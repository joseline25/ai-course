"""
Python Dictionary Comprehension Tutorial


how you can use it to create dictionaries, to replace (nested) for loops or lambda 
functions with map(), filter() and reduce(), ...!


Dictionary comprehension is a method for transforming one dictionary into another
dictionary. During this transformation, items within the original dictionary can 
be conditionally included in the new dictionary, and each item can be transformed
as needed.

The way to do dictionary comprehension in Python is to be able to access the key
objects and the value objects of a dictionary.

How can this be done?

1 - access the keys, values or both from a dictionary (.keys(), .values(), .items())
2 - use the basic template

Python has you covered! You can simply use the built-in methods for the same:
"""

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Put all keys of `dict1` in a list and returns the list
dict_keys = dict1.keys()
# dict_keys(['a', 'b', 'c', 'd'])

print(dict_keys)

# Put all values saved in `dict1` in a list and returns the list
dict_values = dict1.values()

print(dict_values)
# dict_values([1, 2, 3, 4])
# access each key-value pair within a dictionary using the items() method:

print(dict1.items())
# dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

# This is the general template you can follow for dictionary comprehension in Python:

"""
dict_variable = {key:value for (key,value) in dictonary.items()}

This can serve as the basic and the most simple template. This can get more and more
complex as you add conditionalities to it.
"""
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Double each value in the dictionary
double_dict1 = {k: v*2 for (k, v) in dict1.items()}
print(double_dict1)
# {'a': 2, 'b': 4, 'c': 6, 'd': 8, 'e': 10}

# make changes to the key values

dict1_keys = {k*2: v for (k, v) in dict1.items()}
print(dict1_keys)
# {'aa': 1, 'bb': 2, 'cc': 3, 'dd': 4, 'ee': 5}

"""
Why Use Dictionary Comprehension?

Dictionary comprehension is a powerful concept and can be used to substitute for 
loops and lambda functions. However, not all for loops can be written as a dictionary 
comprehension, but all dictionary comprehension can be written with a for loop.



Consider the following problem where you want to create a new dictionary where the key 
is a number divisible by 2 in a range of 0-10, and it's value is the square of the number.

Let's see how you can solve the same problem using a for loop and dictionary comprehension:
"""

# for loop

numbers = range(10)

new_dict_for = {}

for n in numbers:
    if n % 2 == 0:
        new_dict_for[n] = n ** 2  # we have set randomly that value = n**2

print(new_dict_for)
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# dictionary comprehensionn

new_dict_comp = {k: k**2 for k in numbers if k % 2 == 0}
print(new_dict_comp)
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

"""
Alternative to for loops
For loops are used to repeat a certain operation or a block of instructions in 
a program for a given number of times. However, nested for loops (for loop inside
another for loop) can get confusing and complex. Dictionary comprehensions are
better in such situations and can simplify the readability and your understanding
of the code.
"""

# alternative to lambda functions
"""
Lambda functions are a way of creating small anonymous functions. They are functions
without a name. These functions are throw-away functions, which are only needed where
they have been created. Lambda functions are mainly used in combination with the
functions filter(), map() and reduce().
"""

# Initialize `fahrenheit` dictionary
fahrenheit = {'t1': -30, 't2': -20, 't3': -10, 't4': 0}

# Get the corresponding `celsius` values
celsius = list(map(lambda x: (float(5)/9)*(x-32), fahrenheit.values()))

# Create the `celsius` dictionary
celsius_dict = dict(zip(fahrenheit.keys(), celsius))

print(celsius_dict)
# {'t1': -34.44444444444444, 't2': -28.88888888888889, 't3': -23.333333333333336, 't4': -17.77777777777778}

# Adding Conditionals to Dictionary Comprehension

# If Condition
"""
Let's suppose you need to create a new dictionary from a given dictionary but with 
items that are greater than 2. 
"""

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Check for items greater than 2
dict1_cond = {k: v for (k, v) in dict1.items() if v > 2}

print(dict1_cond)
# {'c': 3, 'd': 4, 'e': 5}

# Multiple If Conditions

"""
In the problem above, what if you have to not only get the items greater than 2 but
also need to check if they are multiples of 2 at the same time?
"""

dict1_doubleCond = {k: v for (k, v) in dict1.items() if v > 2 if v % 2 == 0}
print(dict1_doubleCond)
# {'d': 4}

# Let's see one more example with three conditionals: greater than 2,
# multiple of 2 and of 3

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

dict1_tripleCond = {k: v for (k, v) in dict1.items()
                    if v > 2 if v % 2 == 0 if v % 3 == 0}

print(dict1_tripleCond)
# {'f': 6}

# If-Else Conditions

# Identify odd and even entries
dict1_tripleCond = {k: ('even' if v % 2 == 0 else 'odd')
                    for (k, v) in dict1.items()}

print(dict1_tripleCond)
# {'a': 'odd', 'b': 'even', 'c': 'odd', 'd': 'even', 'e': 'odd', 'f': 'even'}

# Nested Dictionary Comprehension
"""
Nesting is a programming concept where data is organized in layers, or where objects
contain other similar objects. You must have often seen a nested 'if' structure, which
is an if condition inside another if condition.

Similarly, dictionaries can be nested, and thus their comprehensions can be nested as well.
"""

nested_dict = {'first': {'a': 1}, 'second': {'b': 2}}
float_dict = {outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items(
)} for (outer_k, outer_v) in nested_dict.items()}
print(float_dict)
