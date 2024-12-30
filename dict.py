students = {
    "name" : "Ethan",
    "age" : 11,
    "height" : 5.1,
    "laptop" : True
}

# 1. They are ordered
# 2. They are changeable
# 3.They do not allow duplicates

#print(students)

# Access Dictionary Items
#print(students["laptop"])

# Using the get method
#print(students.get("name"))

# Getting all keys
# use the keys method
#print(students.keys())

# Getting all values
# use the values method
#print(students.values())

# Getting Items
# using the items method
#print(students.items())

# Changing Dictionary Items
#print["height"] = 5.1

#print(students)

# Using the update method



#print(students)

# Adding Dictionary Items
students["eye-color"] = "red"

students.update({"car" : False})

#print(students)

# Removing Dictionary Items
# Using the pop method
students.pop("laptop")

#using the pop-item method
students.popitem()

#usind the del keyword
del students["eye-color"]

#using the clear method
students.clear()

#print(students)

# Looping through dictionary
for ph in students:
    #print(ph) # print all keys

#for ph in students.keys():
    #print(ph)

#for ph in students:
    #print(students[ph]) # print all values

#for ph in students.values():
    #print(ph)

#for px, py in students.items():
    print(px, py)

# copy a dictionary
students2 = students.copy()
students3 = dict(students)
print(students3)

# nested dictionary 
myFamily = {
    "my father" : {
        "name" : "Kwame",
        "age" : 53,
        "height" : 8.8,
        "food" : "Fufu",
        "dislike" : "Lies"
    },
    "my mother" : {
        "name" : "Anita",
        "age" : 40,
        "height" : 4.5,
        "food" : "Rice and Kontomire",
        "dislike" : "Lies"
    },
    "my self" : {
        "name" : "Ethan",
        "age" : 11,
        "height" : 5.8,
        "food" : "Indomie",
        "Dislike" : "Rice and Kontomire"
    },
    "my sister" : {
        "name" : "Michelle",
        "age" : 7,
        "height" : 4.5,
        "food" : "Candy",
        "dislike" : "Annoying People"
    },
}

print(myFamily["my father"])

for x, details in myFamily.items():
    print(x)

for z in details:
    print(z + ':', details[z])