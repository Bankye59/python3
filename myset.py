mySet = {"apple", "banana", "kiwi", "banana", "mango", "cherry", 6, 4.50, True}
print(mySet)

# Note : The values 1 and true are considered the same value in sets, and are treated as duplicates
# Note : The values 0 and false are considered the same value in sets, and are treated as duplicates

# They are not ordered
# They are unchangeable
# They do not allow duplicates

# Accesing Items
for x in mySet:
    print(x)

if "banana" in mySet:
    print("Yes")

print("banana" in mySet)
print("banana" not in mySet)

# Add items
# Using the add method
mySet.add("orange")
print(mySet)

# remove items
mySet.remove("banana")
print(mySet)

mySet.discard("kiwi")
print(mySet)

print(mySet.pop())

#print(mySet.clear())

#del mySet

#looping
mySet= {"Minions","Spongebob","Despicable me,","Chucky","Annabelle"}

for item in mySet:
    print(item)

# Join Sets
set5 = {1,2,3,4}
set6 = {"a", "b", "c"}

# Union method
myUnion = set5.union(set6)
#or
myUnion = set5 | set6
print(myUnion)

# Quiz
set11 = {1,2,3,4}
set12 = {"a", "b", "c"}
set13 = {9,8,7,6}
set14 = {"d", "m", "v"}
myUnion = set11 | set12 | set13 | set14
print(myUnion)