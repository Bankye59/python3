myTuple = ("Dubai", "South Africa", "New York", "San Francisco")
print(myTuple)

# Adding Items to Tuples
y = list(myTuple)
y.append("Accra")
myTuple = tuple(y)

x = list(myTuple)
x.append("Kumasi")
myTuple = tuple(x)

print(myTuple)

# Unpacking Tuples
(d,*n) = myTuple

print (d)
print(n)