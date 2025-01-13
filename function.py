def myFunction():
    print("Today is Saturday!")
    print("Emerald is in class.")
    print("Ethan is also here.")

myFunction()

def areaOfTriangle(b, h):
    area = 0.5 * b * h
    print(area)

base = float(input("Enter base: "))
height = float(input("Enter heisght: "))
areaOfTriangle(base, height)

# parameters are variables listed in the parenthess in the function definition
# arguments are values

# Arbitary Arguments
def myClass(*students):
    print(students[2] + "is leaving us.")

myClass("Emerald", "Ethan", "Haris", "Maliaka")

# Keyword Argujments
def myPythonClass(student1, student2, student3, student4):
    print(" The youngest student is " + student1)

myPythonClass(student3 = "Mike", student1 = "Sharon", student2= "Nana", student4= "Jason")
              
# Arbitory Keyword Arguments
def myPythonClass(**students)
    print(" The youngest student is " + students["student1"])

myPythonClass(student3 = "Mike", student1 = "Sharon", student2= "Nana", student4= "Jason")

# defaul parameter value
def myFunc(a = 5, b = 10):
    print(a + b)
myFunc()

    