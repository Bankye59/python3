myself = {
    "name" : "Ethan",
    "age" : 11,
    "laptop" : True,
    "location" : "Banana Inn",
    "hobby" : "Drawing",
    "school" : "Dayspring Montessori International School",
    "height" : 4.10,
    "food" : "Indomie",
}

print(myself)

# Access Dictionary Items
print(myself["laptop"])

# Using the get method
print(myself.get("name"))

# Getting all keys
# use the keys method
print(myself.keys())

# Getting all values
# use the values method
print(myself.values())

# Getting Items
# using the items method
print(myself.items())