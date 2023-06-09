# This is 2/5 of the full Python's beginners pack.
# ------------------
# Section 2 - Control Flow and Data Structures
# ------------------

# Lesson 6 - Conditional Statements (if-else)

# Code 1 - Simple if-else
num = int(input("Enter a number: "))
if num > 0:
  print("The number's positive")
else:
  print("The number's negative.")
  
# Code 2 - if-elif-else
marks = int(input("Enter your marks: "))
if marks >= 90:
  print("Grade: A")
elif marks >= 80:
  print("Grade: B")
elif marks >= 70:
  print("Grade: C")
elif marks >= 60:
  print("Grade: D")
else:
  print("Grade: F")
  
# Code 3 - Nested if statements
age = int(input("Enter your age: "))
if age >= 18:
  print("You are eligible for a driving license")
  license_type = input("Do you want a learner's license? (Yes/No): ")
  if license_type.lower() == "yes":
    print("You can apply for a learner's license.")
  else:
    print("You can apply for a permament driving license.")
else:
  print("You are not eligible for a driving license yet.")
  
# Code 4 - Multiple conditions with logical operators
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
  print("It's a leap year.")
else:
  print("It's not a leap year.")

# Code 5 - Ternary operator
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter a second number: "))
meximum = num1 if num1 > num2 else num2
print("The maximum number is: ", maximum)
###################################

# Lesson 7 - Loops (for and while)

# Code 1 - For loop
for num in range(1, 6):
  print(num)
  
# Code 2 - Nested for loop
for i in range(1, 6):
  for j in range(1, 6):
    print(i * j, end="\t")
    print()
    
# Code 3 - While loop with condition
num = 2
while num <= 10:
  print(num)
  num += 2
  
# Code 4 - Break statement
for num in range(1, 6):
  print(num)
  if num == 3:
    break
    
# Code 5 - Continue statement
for num in range(1, 11):
  if num % 2 == 0:
    continue
  print(name)
##################################

# Lesson 8 - Lists

# Code 1 - Accessing lists
items = ["apple", "orange", "banana"]
print(items[0])
print(items[2])

# Code 2 - Modifying (Appending and Removing)
items = ["apple", "orange", "banana"]
items.append("graps")
print("items")

items.remove("orange")
print(items)

# Code 3 - List slicing and indexing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sliced = numbers[2:6]
print(sliced)

numbers[0] = 11
print(numbers)

# Code 4 - Length of a List
items = ["apple", "banana", "orange"]
print(len(items))

# Code 5 - Iterating
items = ["apple", "banana", "orange"]
for item in items:
  print(item)
####################################

# Lesson 9 - Tuples

# Code 1 - Accessing tuples
items = ("apples", "oranges", "banana", "grapes")
print(items[0])
print(items[3])

# Code 2 - Unpacking tuples
point = (3, 4)
x, y = point

print(x)
print(y)

# Code 3 - Iterating
items = ("apples", "oranges", "banana", "grapes")
for item in items:
  print(item)
  
# Code 4 - Tuple methods
items = ("apples", "oranges", "banana", "grapes")
count = items.count("oranges")
index = items.index("grapes")
########################################

# Lesson 10 - Dictionaries

# Code 1 - Accessing dictionaries
person = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
print(person["name"])
print(person["age"])
print(person["city"])

# Code 2 - Modifying
person = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

person["age"] = 31
person["city"] = "Los Angeles"
print(person)

# Code 3 - Adding and deleting items
person = {
  "name": "John",
  "age": 30
}
person["city"] = "New York"
print(person)

def person["age"]
print(person)

# Code 4 - Iterating over dictionaries
person = {
  "name": "John",
  "age": 30.
  "city": "New York"
}

for key in person:
  print(key)
  
for value in person.values():
  print(value)
  
for key, value in person.items():
  print(key, value)
  
# Code 5 - Checking dictionary key existence
person = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

print("name" in person)
print("country" in person)
####################################

# End of section 2
