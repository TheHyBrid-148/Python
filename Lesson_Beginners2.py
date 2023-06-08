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
