# Basic Operations
fruits = ["Grapes", "Orange", "Apple","Mango", "Tangerine"]
print (fruits)

# Stuff 
fruits.append ("Banana")
fruits.remove ("Apple")
print (fruits)

# Slicing
print (fruits[5:4])
print (fruits[9:9])
print (fruits[6:7])

# Numbers
numbers = ["1", "2", "3","4", "5", "6", "7", "8", "9", "10"]
print(numbers)

# Uppercase
#fruits.capitalise("Banana")
#fruits.capitalise("Apple")
#fruits.capitalise("Mango")
#fruits.capitalise("Grapes")
#fruits.capitalise("Tangerine")
#print(fruits)

# Nested lists
myElement = {
    "my father" : {
        "fruit" : "Apple",
        "color" : "Red"
    },
    "my cousin" : {
        "fruit" : "Orange",
        "color" : "Orange"
    },
    "my sister" : {
        "fruit" : "Grape",
        "color" : "Purple"
    },
    "my friend" : {
        "fruit" : "Banana",
        "color" : "Yellow"
    },
}

print(myElement["my father"])

for x, details in myElement.items():
    print(x)

for z in details:
    print(z + ':', details[z])
    
# Dictionary
Ethan = {
    "name" : "Ethan",
    "grade" : 6,
}

Michael = {
    "name" : "Michael",
    "grade" : 6,
}

Michelle = {
    "name" : "Michelle",
    "grade" : 3,
}

print(Ethan, Michael, Michelle)

Kyle = {
    "name" : "Kyle",
    "grade" : 4,
}

print(Ethan, Michael, Michelle, Kyle)

Michael.update({"grade" : 2})

print(Ethan, Michael, Michelle)

Michelle.clear()

print(Ethan, Michael, Michelle)

print(Michelle.values())

Ethan.update({"Ethan" : True})
print(Ethan, Michael, Michelle)

# Stuff Again
for ph in Michelle:
    print(ph)  

for ph in Michelle.keys():
    print(ph)

for ph in Michelle:
    print(Michelle[ph]) 

for ph in Michelle.values():
    print(ph)

print(Michelle)
# Nested Dictionary
Kofi = {
    "Kofi" : {
        "name" : "Kofi",
        "grade" : 8,
        "age" : 12,
        "city" : "Chorkor"
    },
    "Brian" : {
        "name" : "Brian",
        "age" : 11,
        "grade" : 6,
        "city" : "Accra",
    },
}

print("Brian")