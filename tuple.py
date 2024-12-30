myTuple = ("apple", "banana", "kiwi", "banana", "mango", "cherry", 6, 4.50, True)

myTuple2 = ("pineapple",)

print (myTuple)

# Accessing Tuple Items
print (myTuple[:6])

# Updating Tuple
x = list(myTuple)
x[3] = "watermelon"
myTuple = tuple(x)

print(myTuple)

# Adding Items to Tuples
y = list(myTuple)
y.append("pear")
myTuple = tuple(y)

print(myTuple)

# Unpacking Tuples
(c, f, t, g, h, j, k, l, a, s) = myTuple
(r, *p) = myTuple
print(r)
print(p)