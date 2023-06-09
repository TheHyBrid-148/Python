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
