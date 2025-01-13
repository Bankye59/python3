# Tuples
# 1. A tuple in Python is an immutable, ordered collection of elements.Some differences of tuples from lists; 
  # Tuples cannot be changed.
  # Tuples are ordered.
  # Tuples do not allow duplicates.

# Question 2
Fruits = ("Grapes", "Tangerine", "Orange")

# Question 3
print (Fruits[1:2])

# Question 4
# We cannot change the value of a tuple because if they are created you cannot change them.

# Question 5
Numbers = (1,2,3,4,5)
print (Numbers[3:5])

# Question 6
empty_tuple = ()
print(empty_tuple)

# Question 7
# You can contentate a tuple by using addition

# Sets
# 1. A set is an unordered collection of unique elements. It is similar to lists and tuples in that it holds multiple items

# Question 2
colors = {"red", "blue", "orange"}
print(colors)

# Question 3
# To add an element to a set, you use the add method.

# Question 4
# No, you cannot add a duplicate element to a set, If you try to add an element that is already present in the set, the set will ignore the duplicate and the set will remain unchanged.

# Question 5
numbers = {1,2,2,3,4,4,5}
print(numbers)

# Question 6
empty_set = set()

# Question 7
# Yes, you can find the union, intersection, and difference of two sets in Python.

# Mixed Tuple And Sets
# Question 1
mixed_data = ("apple", 42, 3.14, "banana", 42, 3.14)
converted_set = set(mixed_data)