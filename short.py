# 1.Defining a Function
def greet():
    print("Welcome to Python Programming!")
    
greet()

def display_number():
    print(42)

display_number()

# 2. Calling a Function
def say_hello():
    print("Hello, World!")

say_hello()

def add_two_numbers():
    print(10)
    print(20)

add_two_numbers()

# 3. Arguments in Functions
def greet_person(*students):
    print("Hello" + students[0])

greet_person("Alice", "Brian", "Patrick", "John")

def square_number(b, h):
    area = 5 * b * h
    print(area)

# 4. Parameters vs. Arguments
def introduce(first_name, last_name):
    print(f"My name is {first_name} {last_name}")

introduce("Ethan", "Sagoe")