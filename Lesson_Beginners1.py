# This is 1/5 of the full Python's beginners pack.
# ------------------
# Section 1 - Python Basics
# ------------------

# Lesson 1 - Printing statements

# Code 1 - Simple text
print("Hello, world")

# Code 2 - Variable's value
name = "John"
print("My name is ", name)

# Code 3 - Formatting output
age = 25
print("I am ", age, " years old.")

# Code 4 - Multiple values on separate lines
print("First Line")
print("Second Line")
print("Third Line")

# Code 5 - Combination of text and numerics
x = 10
y = 5
sum = x + y
print("The sum of ", x, " and ", y, " is ", sum)
##############################

# Lesson 2 - Data types and Variables

# Code 1 - Assigning values
age = 25 # integers
height = 175

name = "John" # strings/text
country = "USA"

pi = 3.14 # float/decimal values
weight = 68.5

# Code 2 - Numeric operations
x = 10
y = 5

result = x + y # adding
print(result) # Output: 15

result = x - y # subtracting
print(result) # Output: 5 

result = x * y # multiplication
print(result) # Output: 50

result = x / y # division
print(result) # Output: 2.0

result = x // y # Integer/Floor division
print(result) # Output: 2

result = x % y # Remainder
print(result) # Output: 0

result = x ** y # exponent
print(result) # Output: 100000

# Code 3 - String operations
first = "Cole"
last = "Lagman"
full_name = first + " " + last
print(full_name)

repeat_name = first * 3
print(repeat_name)

message = "Hello, Hi!"
print(message[0]) # H
print(message[5]) # ,
print(message[-3]) # H

print(message[2:9]) # llo, Hi

# Code 4 - Multiple assignments
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

a = 10
b = 5

a, b = b, a # switching vatiable values
print(a)
print(b)

# Code 5 - Type conversions
num = 123
num_str = str(num)
print(num_str)

float_num = 3.14
int_num = int(float_num)
print(int_num)

str_num = "100"
int_num = int(str_num)
print(int_num)

str_float = "3.14"
float_num = float(str_float)
print(float_num)
##############################

# Lesson 3 - Operators and Expressions

# Code 1 - Arithmetics
a = 10
b = 5

add = a + b
print(add)
subtract = a - b
print(subtract)
multiply = a * b
print(multiply)
divide = a / b
print(divide)
modulo = a % b
print(modulo)
exponent = a ** b
print(exponent)

# Code 2 - Comparison Operators
a = 10
b = 5

greater = a > b # True
less = a < b # False
greater_or_equal = a >= b # True
less_or_equal = a <= b # False
equal = a == b # False
not_equal = a != b # True

# Code 3 - Logical operators
a = True
b = False

logical_and = a and b # False
logical_or = a or b # True
logical_not_a = not a # False
logical_not_b = not b # True

# Code 4 - Compound operators
a = 10
b = 5

a += b # a = a + b
print(a) # 15

a -= b # a = a - b
print(a) # 10

a *= b # a = a * b
print(a) # 50

a /= b # a = a / b
print(a) # 10.0

a %= b # a = a % b
print(a) # 0.0

a **= b # a = a ** b
print(a) # 0.0

# Code 5 - Operator precedence
result = 10 + 2 * 3 - 4 / 2 ** 2
print(result) # 11.0
##############################

# Lesson 4 - Strings

# Code 1 - String concatenation
first = "John"
last = "Cole"
full = last + " " + last
print(full)

# Code 2 - String Indexing and Slicing
text = "Hello, world"
print(text[5]) # ,
print(text[3:9]) # llo,wo

# Code 3 - String length
text = "Python"
length = len(text)
print(length) # 6

# Code 4 - Converting Case
text = "Python Python"
print(text.upper()) # PYTHON PYTHON
print(text.lower()) # python python
print(text.capitalize()) # Python python

# Code 5 - String formatting
name = "Alice:
age = 17
print("My name is {} and I am {} years old.".format(name, age))
##############################

# Lesson 4 - User Input

# Code 1 - Basic input
name = input("Enter your name: ")
print("Hello " + name, "!")

# Code 2 - Numeric Input and Conversion
age = int(input("Enter your age: "))
years_left = 100 - age
print("You have ", years_left, "years left until you turn 100")

# Code 3 - Handling Float-point input
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilos: "))
bmi = weight / (height ** 2) 
print("Your BMI is: ", bmi)
