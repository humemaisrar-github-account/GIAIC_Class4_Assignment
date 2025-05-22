 
# Functions Example
def greet(name):
    print(f"Hello, {name}!")

greet("Humema")

# Function with return
def add(a, b):
    return a + b

result = add(3, 5)
print("Sum is:", result)

 

# In another file or same one
import mymodule
print("Square:", mymodule.square(4))
 
# Try-Except block
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Please enter a valid number!")

# Try-Except-Finally
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This block always runs.")
 
with open("example.txt", "w") as file:
    file.write("Hello, this is a file.\n")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)

# Appending to a file
with open("example.txt", "a") as file:
    file.write("Adding another line.\n")
 
# Math module
import math
print("Square root of 16:", math.sqrt(16))
print("Power 2^3:", math.pow(2, 3))
print("Pi value:", math.pi)

# Date and time
from datetime import datetime
now = datetime.now()
print("Current Date and Time:", now)

# Calendar
import calendar
print("March 2025 calendar:")
print(calendar.month(2025, 3))
