# This is 3/5 of the full Python's beginners pack.
# ------------------
# Section 3 - Functions, Modules, and File Handling
# ------------------

# Lesson 11 - Functions

# Code 1 - Basic function
def greet():
  print("Welcome!")

greet()

# Code 2 - Function with parameters
def greet(name):
  print("Hello", + name + "Welcome!")

greet("Alice")

# Code 3 - Function with return value
def multiply(a, b):
  return a * b

result = multiply(5, 3)
print("Result: ", result)
