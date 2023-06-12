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

# Code 4 - Recursive function
def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n  * factorial(n - 1)

print("Factorial of 5: ", factorial(5))

# Code 5 - Function with default parameter value
def power(base, exponent=2):
  return base  ** exponent

print("Power of 3: ", power(3))
print("Power of 4 with exponent of 3", power(4, 3))
###################################

# Lesson 12 - Modules and packages

# Code 1 - 
