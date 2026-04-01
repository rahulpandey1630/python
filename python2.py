# ============================================================
# PHASE 1: PYTHON CORE — COMPLETE MENTOR NOTES
# Sheryians Coding School | Roadmap: Python → ML → DL
# ============================================================


# ============================================================
# CHAPTER 1: INSTALLATION & SETUP
# ============================================================

# WHAT IS PYTHON?
# Python is an interpreted language
# Your code (.py file) → converted to bytecode → executed by PVM
# PVM = Python Virtual Machine (installed when you install Python)
# Download from: python.org → select your OS → install

# REAL WORLD ANALOGY:
# Python code = recipe instructions
# PVM = chef who reads and executes that recipe line by line
# This is why Python runs line by line (not all at once like C++)

# WHAT IS AN IDE?
# IDE = Integrated Development Environment
# It is where you write, run, and debug your code
# Options available: VS Code, PyCharm, Jupyter Notebook
# This course uses: VS Code (most popular, lightweight)

# HOW TO SET UP VS CODE FOR PYTHON:
# Step 1: Install Python from python.org
# Step 2: Open VS Code
# Step 3: Go to Extensions (Ctrl+Shift+X)
# Step 4: Install "Python" extension
# Step 5: Install "Code Runner" extension
# Step 6: Now you can run .py files directly inside VS Code

# IMPORTANT INTERVIEW POINT:
# Python is "interpreted" not "compiled"
# Internally: source code → bytecode (.pyc) → PVM executes it
# This makes Python slower than C++ but much faster to write

# COMMON MISTAKE TO AVOID:
# During installation on Windows → always check "Add Python to PATH"
# If you miss this → "python" command won't work in terminal
# Fix: reinstall Python and check that box


# ============================================================
# CHAPTER 2: COMMENTS & VARIABLES
# ============================================================

# ----- COMMENTS -----

# WHAT ARE COMMENTS?
# Comments are lines that Python interpreter IGNORES completely
# Used to explain code, take notes, or temporarily disable code
# Good developers write comments — it's a professional habit

# SINGLE LINE COMMENT:
# Use the # symbol — everything after # on that line is ignored
# Example:
# name = "Akarsh"   ← this entire line is ignored

# MULTILINE COMMENT (Doc String trick):
# Python does NOT have a real multiline comment keyword
# We use triple quotes """ """ as a workaround
# Technically it creates a string that gets ignored at runtime

"""
This is a
multiline docstring
used as a comment
"""

# IMPORTANT: """ """ is actually a string literal, not a true comment
# Real use of """ """ is for function/class documentation (docstrings)
# Interview trick: "Python has no official multiline comment"


# ----- VARIABLES -----

# WHAT IS A VARIABLE?
# A variable is a named container that stores data in memory
# Think of it like a labeled box — the label is the name,
# the content inside is the value

# SYNTAX: variable_name = value
name = "Akarsh"       # stores a string
age = 21              # stores an integer
gpa = 9.2             # stores a float
is_student = True     # stores a boolean

# Python is DYNAMICALLY TYPED
# You don't need to declare the type like in C++ (int x = 5)
# Python figures out the type automatically from the value
x = 10        # Python knows this is int
x = "hello"   # now x is string — Python allows this (dynamic)

# VARIABLE NAMING RULES (strict — breaking these = SyntaxError):
# Rule 1: Cannot start with a number
# 2name = "bad"    ← ERROR

# Rule 2: No spaces allowed
# my name = "bad"  ← ERROR

# Rule 3: No special characters except underscore (_)
# my-name = "bad"  ← ERROR
# my@name = "bad"  ← ERROR

# Rule 4: Cannot use Python reserved keywords
# if = 5    ← ERROR (if is a keyword)
# for = 5   ← ERROR

# Rule 5: Case sensitive
# name = "Alice"
# Name = "Bob"
# NAME = "Charlie"
# All three above are DIFFERENT variables

# VALID VARIABLE EXAMPLES:
my_name = "Akarsh"
_private = "hidden"
number1 = 100
camelCase = "valid but not preferred in Python"

# NAMING CONVENTIONS (3 styles — Python prefers snake_case):

# 1. camelCase → first word lowercase, rest capitalized
#    Example: sheryiansSchool, myVariableName
#    Used in: JavaScript mostly — AVOID in Python

# 2. PascalCase → every word starts with capital
#    Example: SheryiansSchool, MyClassName
#    Used in: Python CLASS names only

# 3. snake_case → all lowercase with underscores
#    Example: sheryians_school, my_variable_name
#    Used in: Python variables and functions — THIS IS STANDARD ✅

# PYTHON CONVENTION SUMMARY:
# Variables → snake_case      → student_name = "Riya"
# Functions → snake_case      → def get_name():
# Classes   → PascalCase      → class StudentRecord:
# Constants → ALL_CAPS        → MAX_SIZE = 100

# REAL WORLD ANALOGY:
# Variable = a locker in a school
# Variable name = locker number (label)
# Variable value = what's stored inside the locker
# You can change what's inside (reassign) anytime

# INTERVIEW QUESTIONS:
# Q1: What is dynamic typing in Python?
# A: Python determines variable type at runtime, not compile time
#    You don't need to specify int/str/float explicitly

# Q2: Does Python have constants?
# A: No built-in constant keyword. Convention is ALL_CAPS
#    Example: PI = 3.14  — but Python won't stop you from changing it

# Q3: Can variable name start with underscore?
# A: Yes — _name is valid. Single underscore = convention for "internal use"
#    Double underscore __name = name mangling in OOP (advanced)

# Q4: What happens when you do x = 5, then x = "hello"?
# A: Python allows it — this is dynamic typing
#    The old integer object gets garbage collected automatically

# PRACTICE PROBLEMS:
# 1. Create variables: your name, age, city, gpa, is_employed
# 2. Try creating an invalid variable name — read the error message
# 3. Create a "constant" for speed of light = 299792458


# ============================================================
# CHAPTER 3: DATA TYPES IN PYTHON
# ============================================================

# WHAT ARE DATA TYPES?
# Data types define WHAT KIND of data a variable holds
# Python has built-in data types — each has different properties
# Python automatically assigns type based on the value (dynamic typing)

# TO CHECK TYPE OF ANY VARIABLE: use type() function
x = 10
print(type(x))    # <class 'int'>

# ===== NUMBERS =====

# 1. INTEGER (int)
# Whole numbers — no decimal, no fraction
# Positive, negative, or zero
age = 21
temperature = -5
count = 0
big_number = 1000000

# 2. FLOAT (float)
# Decimal numbers and fractions
# Any number in p/q form
# Stored in memory using IEEE 754 standard (64-bit)
gpa = 9.2
price = 19.99
pi = 3.14159
negative_float = -2.5

# IMPORTANT FLOAT TRAP (interview favorite):
# print(0.1 + 0.2)   → 0.30000000000000004
# Reason: floats can't be stored exactly in binary
# Fix: use round() or decimal module

# 3. COMPLEX (complex)
# Numbers with real + imaginary part
# Format: real + imaginaryj
c = 3 + 4j
# c.real → 3.0
# c.imag → 4.0
# Used in: signal processing, electrical engineering, quantum computing
# Rarely used in daily Python but important to know

# ===== STRINGS =====

# WHAT IS A STRING?
# A string stores ANY character available on keyboard
# Letters, numbers, symbols, spaces — all stored as characters
# Each character has a Unicode value (unique number)

# HOW TO CREATE STRINGS:
name = "Akarsh"       # double quotes
city = 'Mumbai'       # single quotes — both work the same
message = "It's fine" # use double when string contains apostrophe
code = 'He said "hi"' # use single when string contains double quotes

# WHY STRINGS TAKE MORE MEMORY THAN INT/FLOAT:
# Each character is stored with its own Unicode number
# Example: "A" → Unicode 65, "😊" → Unicode 128522
# int just stores one number — string stores multiple unicodes
# Check unicode: ord("A") → 65
# Convert back: chr(65) → "A"

# ===== BOOLEAN =====

# WHAT IS BOOLEAN?
# Only two possible values: True or False
# Used in conditions, comparisons, logical operations
is_logged_in = True
is_empty = False

# IMPORTANT: True = 1, False = 0 in Python
print(True + True)    # 2
print(True * 5)       # 5
print(False + 10)     # 10

# FALSY VALUES (7 values that evaluate to False):
# These 7 things → bool() returns False
# Everything else → bool() returns True
# 0          → bool(0) = False
# 0.0        → bool(0.0) = False
# False      → bool(False) = False
# ""         → bool("") = False   (empty string)
# []         → bool([]) = False   (empty list)
# {}         → bool({}) = False   (empty dict/set)
# ()         → bool(()) = False   (empty tuple)

# ALL OTHER VALUES ARE TRUTHY:
# bool(1) = True
# bool("hello") = True
# bool([1,2,3]) = True
# bool(-1) = True    ← negative numbers are also truthy!

# INTERVIEW QUESTIONS:
# Q1: What is the difference between int and float?
# A: int = whole number, float = decimal. Division always returns float in Python 3

# Q2: What are falsy values in Python? Name all 7.
# A: 0, 0.0, False, "", [], {}, ()

# Q3: Why does 0.1 + 0.2 != 0.3 in Python?
# A: Floating point precision issue — binary can't represent 0.1 exactly

# Q4: What is Unicode? Why do strings use more memory?
# A: Unicode assigns unique numbers to every character globally
#    Strings store each character as a unicode number → more memory than a single int

# PRACTICE:
# 1. Check type of: 5, 5.0, "5", True, 5+3j
# 2. Find unicode of your name's first letter using ord()
# 3. Check bool() for all 7 falsy values — confirm they all return False
# 4. Try: print(True + True + False + True) — predict before running


# ============================================================
# CHAPTER 4: STRINGS & TYPE CONVERSION
# ============================================================

# ===== HOW STRINGS WORK IN MEMORY =====

# Strings store every character with its own Unicode number
# This is why string takes more memory than int or float
# int stores 1 number, string stores N unicode numbers (N = length)

# Unicode examples:
# ord("A") → 65
# ord("a") → 97
# ord("😊") → 128522
# chr(65) → "A"  (reverse: number to character)

# ===== STRING INDEXING =====

# WHAT IS INDEXING?
# Each character in a string has a position number called INDEX
# Python indexing starts from 0 (not 1!)

# POSITIVE INDEXING (left to right, starts at 0):
a = "Hello"
#    H e l l o
#    0 1 2 3 4
# a[0] → "H"
# a[1] → "e"
# a[4] → "o"

# NEGATIVE INDEXING (right to left, starts at -1):
# a[-1] → "o"   (last character)
# a[-2] → "l"
# a[-5] → "H"   (first character)

# WHY NEGATIVE INDEXING?
# Useful when you don't know the string length
# Getting last character: a[-1] is better than a[len(a)-1]

# REAL WORLD ANALOGY:
# Think of string as a building with floors
# Positive index = ground floor upward (0, 1, 2...)
# Negative index = basement downward (-1, -2, -3...)

# ===== STRING SLICING =====

# WHAT IS SLICING?
# Extracting a portion (slice) of a string
# SYNTAX: string[start : stop : step]
# start → where to begin (inclusive)
# stop  → where to end (EXCLUSIVE — stops before this index)
# step  → how many positions to jump (default = 1)

a = "hello"
# a[1:4:1]  → "ell"  (index 1,2,3 — stops before 4)
# a[1:4]    → "ell"  (step defaults to 1)
# a[0:3]    → "hel"
# a[::2]    → "hlo"  (every 2nd character)
# a[::-1]   → "olleh" (reverse the string! step=-1)
# a[:]      → "hello" (full copy)

# IMPORTANT RULE: stop index is EXCLUSIVE
# a[1:4] → gives index 1, 2, 3 (NOT 4)
# Think: "slice from 1 up to but not including 4"

# INTERVIEW TRICK: 
# How to reverse a string in Python?
# answer = a[::-1]   ← simplest way using slicing

# ===== TYPE CONVERSION =====

# WHAT IS TYPE CONVERSION?
# Converting a variable from one data type to another
# 4 main functions: int(), float(), str(), bool()
# Full list: int(), float(), complex(), str(), list(), tuple(), set(), dict(), bool()

# TYPE 1: IMPLICIT CONVERSION (automatic by Python)
# Python converts automatically when needed
# Example: dividing int by int → result is float automatically
a = 12
result = a / 2
print(result)       # 6.0 (not 6!) — Python auto-converted to float
print(type(result)) # <class 'float'>

# Another example:
x = 5       # int
y = 2.0     # float
z = x + y   # Python converts x to float automatically → 7.0

# WHY? Python promotes to the "larger" type to avoid data loss

# TYPE 2: EXPLICIT CONVERSION (you do it manually)
# You use the conversion functions yourself

# int() examples:
x = "10"
x = int(x)         # "10" → 10 (string to int)
print(x + 5)       # 15

y = 9.9
y = int(y)         # 9.9 → 9 (truncates, does NOT round)
print(y)           # 9

# IMPORTANT: int() truncates (removes decimal) — does NOT round
# int(9.9) = 9, int(9.1) = 9, int(-9.9) = -9

# float() examples:
a = 5
a = float(a)       # 5 → 5.0
b = "3.14"
b = float(b)       # "3.14" → 3.14

# str() examples:
age = 21
age = str(age)     # 21 → "21"
print("Age is: " + age)   # now you can concatenate

# COMMON ERROR WITHOUT CONVERSION:
# print("Age is: " + 21)  ← TypeError! Can't add string + int
# Fix: print("Age is: " + str(21))

# bool() examples:
print(bool(0))     # False
print(bool(1))     # True
print(bool(""))    # False
print(bool("hi"))  # True
# Refer to the 7 falsy values from Chapter 3

# WHAT CANNOT BE CONVERTED:
# int("hello")  → ValueError (not a valid number)
# int("12.5")   → ValueError (has decimal — use float() first)
# float("abc")  → ValueError

# input() ALWAYS RETURNS STRING — very common beginner mistake:
# name = input("Enter name: ")    → string ✅
# age = input("Enter age: ")      → "21" string ❌ for math
# age = int(input("Enter age: ")) → 21 integer ✅ for math

# INTERVIEW QUESTIONS:
# Q1: What is the difference between implicit and explicit type conversion?
# A: Implicit = Python does it automatically (int + float = float)
#    Explicit = programmer does it manually using int(), str() etc.

# Q2: What does int(9.9) return?
# A: 9 — it truncates, does NOT round. Use round() for rounding.

# Q3: What is the default data type of input() in Python?
# A: Always string (str) — must convert manually if you need number

# Q4: Why can't you do "hello" + 5 in Python?
# A: TypeError — Python doesn't auto-convert in concatenation
#    Fix: "hello" + str(5)

# PRACTICE:
# 1. Accept age from user and print "You are X years old" (use int conversion)
# 2. Accept two numbers from user and print their sum (why do you need int()?)
# 3. Try int("hello") — read the error message carefully
# 4. Predict: print(int(True)), print(float(False))


# ============================================================
# CHAPTER 5: INPUT & OUTPUT
# ============================================================

# ===== OUTPUT (print) =====

# print() is the ONLY function to display output in terminal
# Multiple things can be printed separated by comma
name = "Akarsh"
age = 21
print(name)                    # Akarsh
print(name, age)               # Akarsh 21 (space between by default)
print("Name:", name, "Age:", age)  # Name: Akarsh Age: 21

# f-string (formatted string) — BEST WAY to print variables:
# prefix string with f → use {variable} inside
print(f"Hello {name}, you are {age} years old")
# Output: Hello Akarsh, you are 21 years old

# f-string with expression:
x = 10
print(f"Double of x is {x * 2}")  # Double of x is 20

# Other print options:
print("Hello", end="")        # no newline at end (default end="\n")
print("A", "B", sep="-")      # A-B (custom separator, default sep=" ")

# ===== INPUT =====

# input() asks user to type something
# The text inside input("...") is the PROMPT shown to user
# ALWAYS returns a STRING — this is critical to remember

name = input("Enter your name: ")    # stores as string
print(f"Hello {name}!")

# Getting number from user — MUST convert:
age = int(input("Enter your age: "))      # convert to int
price = float(input("Enter price: "))     # convert to float

# REAL WORLD EXAMPLE:
# age = input("Enter age: ")
# print(age + 1)   ← ERROR: can't add string + int
# Fix: age = int(input("Enter age: "))
# print(age + 1)   ← works: 22

# PRACTICE PROBLEMS (from book):
# Q1: Accept two numbers from user, print their sum
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"Sum = {num1 + num2}")

# Q2: Accept age from user and print it
age = int(input("Enter your age: "))
print(f"Your age is {age}")

# INTERVIEW QUESTIONS:
# Q1: What does input() always return?
# A: Always a string (str) regardless of what user types

# Q2: How do you accept multiple inputs in one line?
# A: a, b = input("Enter two numbers: ").split()
#    a, b = int(a), int(b)

# Q3: What is f-string? When was it introduced?
# A: Formatted string literals, introduced in Python 3.6
#    Allows embedding expressions inside {} within a string prefixed with f


# ============================================================
# CHAPTER 6: OPERATORS
# ============================================================

# WHAT ARE OPERATORS?
# Operators are symbols that perform operations on variables/values
# Python has 5 main types

# ===== 1. ARITHMETIC OPERATORS =====
# Used for mathematical calculations
a = 12
b = 5

# +   addition:          a + b  = 17
# -   subtraction:       a - b  = 7
# *   multiplication:    a * b  = 60
# /   division:          a / b  = 2.4  (ALWAYS returns float in Python 3)
# //  floor division:    a // b = 2    (removes decimal — truncates)
# %   modulus:           a % b  = 2    (remainder after division)
# **  exponentiation:    a ** b = 248832 (a to the power b)

# IMPORTANT: / always returns float even if result is whole number
print(10 / 2)    # 2.0 (not 2!)
print(10 // 2)   # 2 (use // for integer division)

# MODULUS USE CASE (very commonly used):
# Check if number is even: number % 2 == 0
# Check if number is odd: number % 2 != 0
# Get last digit of number: number % 10
# Remove last digit: number // 10

# ===== 2. ASSIGNMENT OPERATORS =====

# Basic assignment: =
x = 10    # assigns 10 to x

# Compound assignment operators (shortcut for reassigning):
# These combine arithmetic + assignment in one step

x = 10
x += 5    # same as: x = x + 5   → x is now 15
x -= 3    # same as: x = x - 3   → x is now 12
x *= 2    # same as: x = x * 2   → x is now 24
x /= 4    # same as: x = x / 4   → x is now 6.0
x //= 2   # same as: x = x // 2
x %= 3    # same as: x = x % 3
x **= 2   # same as: x = x ** 2

# WHY USE COMPOUND OPERATORS?
# Cleaner code, less repetition
# Common in loops: counter += 1 instead of counter = counter + 1

# ===== 3. COMPARISON OPERATORS (Relational) =====
# Compare two values of SimilAR TYPE— ALWAYS returns True or False (Boolean)
 
# ==   equal to:               5 == 5   → True
# !=   not equal to:           5 != 3   → True
# >    greater than:           5 > 3    → True
# <    less than:              3 < 5    → True
# >=   greater than or equal:  5 >= 5   → True
# <=   less than or equal:     3 <= 5   → True

# IMPORTANT: == checks VALUE equality (not identity)
# = is assignment, == is comparison (common beginner mistake)
x = 5      # assignment
x == 5     # comparison → True

# STRINGS use ASCII/Unicode values for c omparison:
print("apple" < "banana")   # True (a < b in ASCII)
print("A" < "a")            # True (A=65, a=97 in ASCII)

# ===== 4. LOGICAL OPERATORS =====
# Combine multiple conditions — return True or False

# and → True only if BOTH conditions are True
# or  → True if AT LEAST ONE condition is True
# not → reverses/negates the boolean value

age = 20
salary = 50000

# and example:
print(age > 18 and salary > 30000)   # True (both true)
print(age > 18 and salary > 80000)   # False (second is false)

# or example:
print(age > 18 or salary > 80000)    # True (first is true)
print(age < 18 or salary > 80000)    # False (both false)

# not example:
print(not True)     # False
print(not False)    # True
print(not (age > 18))  # False (reverses True to False)

# TRUTH TABLE FOR and:
# True  and True  = True
# True  and False = False
# False and True  = False
# False and False = False

# TRUTH TABLE FOR or:
# True  or True  = True
# True  or False = True
# False or True  = True
# False or False = False

# SHORT CIRCUIT EVALUATION (interview topic):
# and: if first condition is False → Python SKIPS second condition
# or:  if first condition is True  → Python SKIPS second condition
# This is for performance optimization

# TRIVIAL QUESTION ANSWERS (from book):
# print(126 > 130)                       → False
# print((456 == 456) != (235 == 236))    → print(True != False) → True
# print(12 < 10 or 45 == 56 or 69 > 70 or 15 != 13)
#   → False or False or False or True → True
# print(True and bool(0))                → True and False → False

# INTERVIEW QUESTIONS:
# Q1: What is the difference between = and == in Python?
# A: = is assignment operator, == is comparison (equality check)

# Q2: What is short-circuit evaluation?
# A: In 'and' — if first is False, second isn't evaluated
#    In 'or' — if first is True, second isn't evaluated

# Q3: What does "and" return? Is it always True/False?
# A: Actually returns one of the operands, not necessarily True/False
#    5 and 0 → 0 (returns first falsy value)
#    5 and 3 → 3 (returns last truthy value)
#    This is advanced but good for interviews

# PRACTICE:
# 1. Write expression to check if number is between 10 and 20
# 2. Check if a string is NOT empty
# 3. Solve all 4 trivial questions from book before looking at answers


# ============================================================
# CHAPTER 7: CONDITIONAL STATEMENTS
# ============================================================

# WHAT ARE CONDITIONAL STATEMENTS?
# Allow decision-making in programs
# Execute different code blocks based on whether conditions are True/False
# Also called: Control Flow Statements

# REAL WORLD ANALOGY:
# You receive a number from user
# If number > 10 → do Task A
# If number < 10 → do Task B
# The number decides which path to take — that's control flow

# ===== TYPES OF CONDITIONAL STATEMENTS =====

# 1. if → executes block ONLY if condition is True
# 2. if-else → one block for True, another for False
# 3. if-elif-else → checks multiple conditions in sequence

# ===== 1. if STATEMENT =====
# SYNTAX:
# if condition:
#     # code runs if condition is True
#     # INDENTATION IS MANDATORY (4 spaces or 1 tab)

age = 20
if age >= 18:
    print("You are an adult")    # this runs because 20 >= 18 is True

# If condition is False → nothing happens, code below if continues
x = 5
if x > 10:
    print("Greater")    # this does NOT run
print("After if")       # this always runs

# ===== 2. if-else STATEMENT =====
# SYNTAX:
# if condition:
#     # code if True
# else:
#     # code if False

marks = 45
if marks >= 50:
    print("Pass")
else:
    print("Fail")    # this runs because 45 < 50

# ===== 3. if-elif-else STATEMENT =====
# elif = "else if" — checks another condition
# Can have multiple elif blocks

marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")    # this runs — 75 >= 70 is True
elif marks >= 60:
    print("Grade D")
else:
    print("Fail")       # only runs if ALL above conditions are False

# IMPORTANT: Python checks conditions TOP TO BOTTOM
# Stops at FIRST True condition and executes that block
# Rest of elif/else are SKIPPED after a match
    
# INDENTATION RULE — CRITICAL IN PYTHON:
# Python uses indentation (spaces) to define code blocks
# Other languages use {} — Python uses spaces/tabs
# Standard: 4 spaces per level
# Mixing tabs and spaces = TabError

# LOGICAL OPERATORS IN CONDITIONS:
age = 20
income = 50000
if age >= 18 and income >= 30000:
    print("Eligible for loan")

# ===== if-elif LADDER =====
# Multiple elif = "elif ladder"
# Used when you have many conditions to check in sequence

temp = 35
if temp < 0:
    print("Freezing Cold ❄️")
elif temp < 10:
    print("Very Cold 🧥")
elif temp < 20:
    print("Cold 🧤")
elif temp < 30:
    print("Pleasant ☁️")
elif temp < 40:
    print("Hot 🔥")
else:
    print("Very Hot 🌞")

# PRACTICE PROBLEMS (from book):
# Q1: Accept two numbers — print the greater one
a = int(input("Enter first: "))
b = int(input("Enter second: "))
if a > b:
    print(f"{a} is greater")
elif b > a:
    print(f"{b} is greater")
else:
    print("Both are equal")

# Q2: Accept gender (M/F) — print greeting
gender = input("Enter gender (M/F): ")
if gender == "M" or gender == "m":
    print("Good Morning Sir")
elif gender == "F" or gender == "f":
    print("Good Morning Ma'am")
else:
    print("Invalid input")

# Q3: Check even or odd
num = int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q4: Valid voter check
name = input("Enter name: ")
age = int(input("Enter age: "))
if age >= 18:
    print(f"Hello {name}, you are a valid voter")
else:
    print(f"Hello {name}, you are NOT a valid voter")

# Q5: Leap year check
# Leap year conditions:
# divisible by 4 AND (not divisible by 100 OR divisible by 400)
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# INTERVIEW QUESTIONS:
# Q1: What is indentation in Python? Why is it important?
# A: Python uses indentation instead of {} to define code blocks
#    Incorrect indentation = IndentationError (program won't run)

# Q2: Can if exist without else?
# A: Yes — else is optional. if can stand alone.

# Q3: Is elif mandatory?
# A: No — it's optional. Used only when you have multiple conditions to check.

# Q4: What happens if multiple elif conditions are True?
# A: Only the FIRST matching elif block executes. Rest are skipped.


# ============================================================
# CHAPTER 8: LOOPS
# ============================================================

# WHAT ARE LOOPS?
# Loops execute a block of code MULTIPLE TIMES without rewriting it
# Without loops: print "hello" 100 times = 100 lines of code
# With loops: print "hello" 100 times = 2 lines of code

# TWO TYPES OF LOOPS IN PYTHON: for and while

# BUCKET ANALOGY (from book):
# You have bucket A full of water, bucket B empty
# Scenario 1: Transfer exactly 4 mugs → you KNOW the count → FOR loop
# Scenario 2: Transfer ALL water → you don't know count, stop when empty → WHILE loop

# ===== RANGE() FUNCTION (needed before for loop) =====

# range() generates a sequence of numbers
# SYNTAX: range(start, stop, step)
# start → where to begin (default = 0)
# stop  → where to end (EXCLUSIVE — doesn't include this value)
# step  → how many to jump (default = 1)

# Examples:
# range(5)       → 0, 1, 2, 3, 4         (0 to 4, not 5)
# range(1, 6)    → 1, 2, 3, 4, 5         (1 to 5, not 6)
# range(1, 10, 2)→ 1, 3, 5, 7, 9         (step of 2)
# range(10, 0, -1)→ 10, 9, 8, 7...1      (reverse)

# IMPORTANT: stop is EXCLUSIVE (same as string slicing rule)
# range(1, 6) gives 1,2,3,4,5 → NOT 6

# ===== FOR LOOP =====

# WHEN TO USE? When you KNOW how many iterations you need
# SYNTAX:
# for variable in sequence:
#     # code to execute

# Example 1: print 1 to 5
for i in range(1, 6):
    print(i)    # prints 1, 2, 3, 4, 5

# Example 2: print "hello" 3 times
for i in range(3):
    print("hello")   # prints hello 3 times

# LOOPING OVER STRINGS — 2 WAYS:
a = "Nature"

# Way 1: Using index values with range
for i in range(len(a)):     # len("Nature") = 6, range(6) = 0,1,2,3,4,5
    print(a[i])             # prints N, a, t, u, r, e (one per line)

# Way 2: Directly iterate over string (simpler)
for char in a:
    print(char)    # gives direct access to character, not index

# DIFFERENCE BETWEEN THE TWO WAYS:
# Way 1: variable i = index (0,1,2...) — you access a[i]
# Way 2: variable char = actual character ("N","a","t"...) — no indexing needed

# WHICH TO USE?
# Need index: use Way 1
# Just need characters: use Way 2 (simpler, more Pythonic)

# ===== BREAK, CONTINUE, ELSE IN LOOPS =====

# RACE TRACK ANALOGY:
# You must complete 20 laps
# break   = it starts raining at lap 16 → you STOP immediately
# continue= you skip lap 16 but complete all other laps
# else    = runs only if you finished ALL laps without break

# BREAK: exits the loop immediately
for i in range(1, 21):
    if i == 16:
        print("It's raining! Stopping at lap", i)
        break           # loop ends here — laps 17,18,19,20 never run
    print(f"Lap {i}")

# CONTINUE: skips current iteration, continues to next
for i in range(1, 21):
    if i == 16:
        print(f"Skipping lap {i}")
        continue        # skips rest of code for i=16, goes to i=17
    print(f"Lap {i}")

# ELSE WITH LOOP: runs ONLY if loop completed without break
for i in range(1, 6):
    print(i)
else:
    print("Loop completed successfully!")   # runs because no break

for i in range(1, 6):
    if i == 3:
        break
    print(i)
else:
    print("This will NOT print")  # doesn't run because break was hit

# ===== FOR LOOP PRACTICE QUESTIONS (from book) =====

# Q1: Accept n, print "hello world" n times
n = int(input("Enter n: "))
for i in range(n):
    print("hello world")

# Q2: Print natural numbers 1 to n
n = int(input("Enter n: "))
for i in range(1, n+1):
    print(i)

# Q3: Reverse for loop — print n to 1
n = int(input("Enter n: "))
for i in range(n, 0, -1):
    print(i)

# Q4: Multiplication table of a number
num = int(input("Enter number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Q5: Sum up to n terms
n = int(input("Enter n: "))
total = 0
for i in range(1, n+1):
    total += i
print(f"Sum = {total}")

# Q6: Factorial of a number
n = int(input("Enter n: "))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(f"{n}! = {factorial}")

# Q7: Sum of all even and odd numbers in range separately
n = int(input("Enter n: "))
even_sum = 0
odd_sum = 0
for i in range(1, n+1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print(f"Even sum = {even_sum}, Odd sum = {odd_sum}")

# Q8: All factors of a number
n = int(input("Enter number: "))
for i in range(1, n+1):
    if n % i == 0:
        print(i)

# Q9: Check if perfect number
# Perfect number = sum of factors (excluding itself) equals the number
# Example: 6 → factors: 1,2,3 → 1+2+3 = 6 ✅
n = int(input("Enter number: "))
factor_sum = 0
for i in range(1, n):    # range(1, n) excludes n itself
    if n % i == 0:
        factor_sum += i
if factor_sum == n:
    print(f"{n} is a Perfect Number")
else:
    print(f"{n} is NOT a Perfect Number")

# Q10: Check if prime number
# Prime = divisible only by 1 and itself
n = int(input("Enter number: "))
is_prime = True
if n < 2:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{n} is Prime")
else:
    print(f"{n} is Not Prime")

# OPTIMIZED PRIME CHECK (only check up to sqrt):
# for i in range(2, int(n**0.5) + 1):
# Because if n has a factor > sqrt(n), the other factor < sqrt(n)
# This reduces iterations significantly for large numbers

# Q11: Reverse a string without built-in functions
s = input("Enter string: ")
reversed_s = ""
for i in range(len(s)-1, -1, -1):
    reversed_s += s[i]
print(reversed_s)

# Q12: Check palindrome
s = input("Enter string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Q13: Count letters, digits, special symbols in string
s = "P@#yn26at^&i5ve"
letters = 0
digits = 0
symbols = 0
for char in s:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    else:
        symbols += 1
print(f"Letters={letters}, Digits={digits}, Symbols={symbols}")

# ===== WHILE LOOP =====

# WHEN TO USE? When you DON'T know how many iterations needed
# You know a CONDITION to stop — not the count
# SYNTAX:
# while condition:
#     # code
#     # MUST update condition variable to avoid infinite loop!

# Basic example:
i = 1
while i <= 5:
    print(i)
    i += 1    # CRITICAL: without this → infinite loop!

# WHILE LOOP HAS: break, continue, else — same as for loop

# WHILE LOOP PRACTICE QUESTIONS (from book):

# Q1: Separate each digit of a number and print on new line
n = int(input("Enter number: "))
while n > 0:
    digit = n % 10      # get last digit
    print(digit)
    n = n // 10         # remove last digit

# Q2: Reverse a number
n = int(input("Enter number: "))
reversed_n = 0
while n > 0:
    digit = n % 10
    reversed_n = reversed_n * 10 + digit
    n = n // 10
print(reversed_n)

# Q3: Palindrome number check
n = int(input("Enter number: "))
original = n
reversed_n = 0
while n > 0:
    digit = n % 10
    reversed_n = reversed_n * 10 + digit
    n = n // 10
if original == reversed_n:
    print("Palindrome number")
else:
    print("Not palindrome")

# Q4: Random number guessing game
import random
secret = random.randint(1, 100)
guess = 0
attempts = 0
while guess != secret:
    guess = int(input("Guess the number (1-100): "))
    attempts += 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You got it in {attempts} attempts!")

# INTERVIEW QUESTIONS (Loops):
# Q1: What is the difference between for and while loop?
# A: for = used when iterations count is known, iterates over a sequence
#    while = used when iterations count is unknown, runs on a condition

# Q2: What happens if you forget to update the condition in a while loop?
# A: Infinite loop — program runs forever, crashes the system
#    Always ensure the condition eventually becomes False

# Q3: What does break do vs continue?
# A: break = exits loop entirely
#    continue = skips CURRENT iteration, goes to next iteration

# Q4: When does the else block of a loop execute?
# A: Only when loop completes WITHOUT hitting a break statement
#    If break is executed, else block is skipped

# Q5: Can you use for loop without range?
# A: Yes — for item in list/string/tuple/dict etc.
#    range is needed only when iterating over numbers


# ============================================================
# CHAPTER 9: FUNCTIONS
# ============================================================

# WHAT ARE FUNCTIONS?
# A function is a reusable block of code with a name
# You define it once, call it many times
# Avoids repetition → makes code modular and readable

# BUILT-IN FUNCTIONS (Python provides these):
# print(), input(), len(), type(), int(), float(), str(), range(), etc.

# USER-DEFINED FUNCTIONS (you create these):
# Use 'def' keyword followed by function name and parentheses

# BASIC SYNTAX:
# def function_name():
#     # code block (indented)

def greet():
    print("Hello, welcome to Python!")

greet()    # calling the function → prints the message
greet()    # call again → prints again (reusability!)

# ===== PARAMETERS AND ARGUMENTS =====

# PARAMETERS: variables listed inside the function definition
# They act as placeholders for incoming values

# ARGUMENTS: actual values passed when calling the function

def greet_person(name):    # 'name' is the PARAMETER
    print(f"Hello {name}!")

greet_person("Alice")    # "Alice" is the ARGUMENT
greet_person("Bob")      # "Bob" is the ARGUMENT

# MULTIPLE PARAMETERS:
def introduce(name, age):
    print(f"I am {name} and I am {age} years old")

introduce("Akarsh", 21)   # positional: 1st arg → name, 2nd → age

# MUST provide same number of arguments as parameters
# introduce("Akarsh")  ← TypeError: missing argument 'age'

# ===== TYPES OF ARGUMENTS =====

# 1. POSITIONAL ARGUMENTS:
# Arguments matched by position — first arg → first param, etc.
def add(a, b):
    return a + b

print(add(3, 5))    # 3 → a, 5 → b → returns 8

# 2. KEYWORD ARGUMENTS:
# Arguments matched by name — order doesn't matter
def introduce(name, age):
    print(f"I am {name}, age {age}")

introduce(age=25, name="John")    # order swapped but named correctly

# 3. DEFAULT ARGUMENTS:
# Parameter has a default value — used if no argument provided
def greet(name="Guest"):
    print(f"Hello {name}!")

greet()          # uses default → "Hello Guest!"
greet("Alice")   # overrides default → "Hello Alice!"

# IMPORTANT RULE: Default parameters must come AFTER non-default ones
# def func(x=5, y): ← SyntaxError! Non-default after default not allowed
# def func(y, x=5): ← This is CORRECT

# ===== RETURN STATEMENT =====

# return sends a value BACK to where the function was called
# Without return → function returns None by default

def add(a, b):
    return a + b       # sends the result back

result = add(3, 5)     # result = 8 (returned value is stored)
print(result)          # 8

# DIFFERENCE: print vs return
# print → shows value on screen but doesn't save it
# return → sends value back to caller, can be stored/used

# Function can return multiple values:
def min_max(lst):
    return min(lst), max(lst)   # returns a tuple

low, high = min_max([3, 1, 7, 2])
print(low, high)   # 1 7

# ===== PRACTICE QUESTIONS =====

# Q1: Function to check even or odd
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

# Q2: Function to find factorial
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Q3: Function to check prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# INTERVIEW QUESTIONS:
# Q1: What is the difference between parameter and argument?
# A: Parameter = variable in function definition (placeholder)
#    Argument = actual value passed when calling function

# Q2: What does a function return if there is no return statement?
# A: Returns None (Python's null value)

# Q3: What are default arguments? Any restrictions?
# A: Default value for parameter if no argument provided
#    Restriction: must come AFTER non-default parameters

# Q4: What is the difference between return and print?
# A: print → displays output to screen, returns None
#    return → sends value back to caller, can be stored and used later


# ============================================================
# CHAPTER 10: DATA STRUCTURES OVERVIEW
# ============================================================

# WHY DATA STRUCTURES?
# Variables store ONE value at a time
# Data structures store MULTIPLE values in one variable
# Python has 4 built-in data structures:
# 1. List      → ordered, mutable, duplicates allowed
# 2. Tuple     → ordered, immutable, duplicates allowed
# 3. Set       → unordered, mutable, NO duplicates
# 4. Dictionary→ ordered (Python 3.7+), mutable, unique keys

# ALSO: custom DSA = Stack, Queue, Linked List, Graph, Tree
# This course covers only built-in ones (not DSA)

# QUICK COMPARISON TABLE:
# Structure | Ordered | Mutable | Duplicates | Syntax
# List      |   Yes   |   Yes   |    Yes     |  []
# Tuple     |   Yes   |   No    |    Yes     |  ()
# Set       |   No    |   Yes   |    No      |  {}
# Dict      |   Yes   |   Yes   | Keys: No   |  {k:v}


# ============================================================
# CHAPTER 11: LIST
# ============================================================

# LIST PROPERTIES:
# Mutable     → can change values after creation
# Ordered     → maintains insertion order, has index
# Duplicates  → allows same value multiple times
# Heterogeneous → can store different data types

# CREATE A LIST:
fruits = ["apple", "banana", "cherry"]
numbers = [10, 20, 30, 40]
mixed = [1, "hello", 3.14, True]    # heterogeneous list
empty = []                           # empty list

# INDEXING AND SLICING (same as strings):
# fruits[0]   → "apple"
# fruits[-1]  → "cherry"
# fruits[1:3] → ["banana", "cherry"]

# LIST IS MUTABLE — strings are not:
numbers[1] = 99    # changes index 1 from 20 to 99
print(numbers)     # [10, 99, 30, 40]
# "hello"[0] = "H"  ← TypeError! strings are immutable

# TRAVERSAL (same 2 ways as strings):
# Way 1: using range and index
for i in range(len(fruits)):
    print(fruits[i])

# Way 2: directly
for fruit in fruits:
    print(fruit)

# LIST METHODS (most important):
numbers = [5, 2, 9, 1, 5, 6]

numbers.append(10)          # adds 10 at the END
numbers.insert(2, 15)       # inserts 15 at index 2
numbers.extend([20, 25])    # adds multiple elements at end
numbers.remove(5)           # removes FIRST occurrence of 5
popped = numbers.pop(3)     # removes and RETURNS element at index 3
idx = numbers.index(6)      # returns index of first occurrence of 6
cnt = numbers.count(5)      # counts occurrences of 5
numbers.sort()              # sorts ascending (in-place)
numbers.reverse()           # reverses order (in-place)
copy = numbers.copy()       # creates a shallow copy
numbers.clear()             # removes ALL elements → []

# DIFFERENCE: remove vs pop
# remove(value) → removes by VALUE, returns nothing
# pop(index)    → removes by INDEX, RETURNS the removed element

# DIFFERENCE: sort() vs sorted()
# numbers.sort()       → modifies original list (in-place)
# sorted(numbers)      → returns new sorted list, original unchanged

# PRACTICE QUESTIONS (from book):
# Q1: Print positive and negative elements separately
nums = [3, -1, 7, -4, 2, -8, 5]
for n in nums:
    if n > 0:
        print(f"Positive: {n}")
    else:
        print(f"Negative: {n}")

# Q2: Mean of list elements
nums = [10, 20, 30, 40, 50]
mean = sum(nums) / len(nums)
print(f"Mean = {mean}")

# Q3: Find greatest element and its index
nums = [3, 7, 1, 9, 4]
max_val = max(nums)
max_idx = nums.index(max_val)
print(f"Greatest = {max_val} at index {max_idx}")

# Q4: Find second greatest

nums = [3, 7, 1, 9, 4]                     # original list of numbers

nums_sorted = sorted(set(nums), reverse=True)  
# set(nums) → removes duplicates (if any)
# sorted(...) → sorts the numbers
# reverse=True → sorts in descending order (largest → smallest)
# result → [9, 7, 4, 3, 1]

print(f"Second greatest = {nums_sorted[1]}")  
# nums_sorted[1] → second element in sorted list
# index 0 → largest (9)
# index 1 → second largest (7)
# prints → Second greatest = 7

'''
def find_largest_and_second(arr):
    largest = float('-inf')      # initialize largest as smallest possible number
    second = float('-inf')       # initialize second largest also as smallest

    for num in arr:              # loop through each number in the list
        
        if num > largest:        # if current number is greater than largest
            second = largest     # old largest becomes second largest
            largest = num        # update largest to current number
        
        elif num > second and num != largest:  
            # if number is:
            # 1. greater than second largest
            # 2. NOT equal to largest (to avoid duplicates)
            second = num         # update second largest

    return largest, second       # return both values


# Example input
arr = [10, 5, 20, 8, 20, 15]

result = find_largest_and_second(arr)  # call function
print(result)                          # print result
'''

# Q5: Check if list is sorted
nums = [1, 2, 3, 4, 5]
print(nums == sorted(nums))   # True if already sorted


'''def is_sorted(nums):
    for i in range(len(nums) - 1):          # loop till second last element
        if nums[i] > nums[i + 1]:           # if current > next → not sorted
            return False                   # immediately return False
    return True                            # if no violation → sorted


# Example
nums = [1, 2, 3, 4, 5]
print(is_sorted(nums))                     # True
'''


# INTERVIEW QUESTIONS:
# Q1: What is the difference between list and tuple?
# A: List = mutable (can change), Tuple = immutable (cannot change)
#    List = [], Tuple = ()

# Q2: What is the difference between append() and extend()?
# A: append(x) → adds x as single element
#    extend([x,y]) → adds each element of iterable individually
#    [1,2].append([3,4]) → [1,2,[3,4]]   (nested)
#    [1,2].extend([3,4]) → [1,2,3,4]     (flat)

# Q3: Is list mutable? What does that mean?
# A: Yes — values can be changed after creation
#    lst[0] = 99 is valid for list, invalid for string/tuple


# ============================================================
# CHAPTER 12: TUPLE
# ============================================================

# TUPLE PROPERTIES:
# Immutable    → CANNOT change values after creation
# Ordered      → has index, maintains order
# Duplicates   → allowed
# Heterogeneous→ can store different types

# CREATE A TUPLE:
t = (5, 2, 9, 1, 5, 6)
t2 = (1, "hello", 3.14)
t3 = ()             # empty tuple
t4 = (5,)           # SINGLE element tuple — MUST have comma!
# t5 = (5)          # this is just integer 5, NOT a tuple

# TUPLE INDEXING AND SLICING — same as list:
# t[0] → 5, t[-1] → 6

# TUPLE IS IMMUTABLE:
# t[0] = 99    ← TypeError: tuple does not support item assignment

# TUPLE METHODS — only 2:
idx = t.index(9)     # finds index of first occurrence of 9
cnt = t.count(5)     # counts occurrences of 5

# WHY USE TUPLE OVER LIST?
# 1. Immutability = safety (data won't be accidentally changed)
# 2. Faster than list (less memory overhead)
# 3. Can be used as dictionary keys (list cannot — list is unhashable)
# 4. Good for returning multiple values from function


# =========================================
# 1. TWO WAYS TO TRAVERSE A TUPLE
# =========================================

# --------- METHOD 1: Direct Traversal ---------
# We directly iterate over elements
t = (5, 2, 9, 1, 5, 6)
for item in t:
    # item will contain each element one by one
    print(item)

# Example output:
# 5 2 9 1 5 6


# --------- METHOD 2: Index-Based Traversal ---------
# We use index positions (like arrays)

for i in range(len(t)):
    # t[i] accesses element at index i
    print(t[i])

# Example output:
# 5 2 9 1 5 6


# =========================================
# 2. IMMUTABILITY (VERY IMPORTANT)
# =========================================

# Tuples cannot be modified after creation

# t[0] = 100   # ❌ ERROR
# Reason: tuple does not support item assignment


# =========================================
# 3. TUPLE METHODS (ONLY 2 IMPORTANT ONES)
# =========================================

# --------- METHOD 1: index() ---------
# Finds FIRST occurrence of element

index_of_9 = t.index(9)
print(index_of_9)   # Output: 2

# If element not found → gives error


# --------- METHOD 2: count() ---------
# Counts how many times element appears

count_of_5 = t.count(5)
print(count_of_5)   # Output: 2


# =========================================
# 4. WHAT TUPLE DOES NOT SUPPORT
# =========================================

# t.append(10)    # ❌ Not allowed
# t.remove(5)     # ❌ Not allowed
# t.sort()        # ❌ Not allowed

# Reason: tuple is immutable


# =========================================
# 5. WHY USE TUPLE (INTERVIEW POINT)
# =========================================

# - Faster than list (less overhead)
# - Safe (data cannot be changed accidentally)
# - Used when values are fixed (like coordinates)




# TUPLE PACKING AND UNPACKING:
coordinates = (10, 20, 30)   # packing
x, y, z = coordinates        # unpacking → x=10, y=20, z=30



# INTERVIEW QUESTIONS:
# Q1: Can you change a tuple after creation?
# A: No — tuples are immutable. But if tuple contains a list,
#    you can change the list's elements (mutable inside immutable)

# Q2: What is the difference between (5) and (5,)?
# A: (5) = integer 5, just parentheses
#    (5,) = tuple with one element — comma makes it a tuple

# Q3: When would you use a tuple instead of a list?
# A: When data should not change (coordinates, RGB colors, DB records)
#    As dictionary keys (lists can't be keys — not hashable)
#    For performance (tuples are faster)


# ============================================================
# CHAPTER 13: SET
# ============================================================

# SET PROPERTIES:
# Mutable      → can add/remove elements
# Unordered    → NO index, NO guarantee of order
# NO duplicates → automatically removes duplicates (unique elements only)
# Semi-heterogeneous → can store strings, numbers, tuples but NOT lists/dicts

# CREATE A SET:
s = {1, 2, 3}
s2 = {1, 2, 2, 3, 3}    # duplicates removed → {1, 2, 3}
s3 = set()              # empty set — MUST use set(), not {} (that's dict!)

# HOW SET STORES DATA (HASHING):
# Every value is hashed using hash() → converted to a number
# That hash number is used as memory index
# Since hash doesn't maintain order → set is UNORDERED
# Mutable objects (list, dict) can't be hashed → can't be stored in set

# SET TRAVERSAL:
# Cannot use index! (unordered)
for item in s:
    print(item)   # order may vary each time

# SET METHODS:
s = {1, 2, 3}
s.add(4)              # adds single element
s.remove(2)           # removes 2 — ERROR if 2 doesn't exist
s.discard(5)          # removes 5 — NO error if not found
popped = s.pop()      # removes and returns a RANDOM element
s.clear()             # removes all elements

# DIFFERENCE: remove vs discard
# remove(x) → raises KeyError if x not in set
# discard(x) → silently ignores if x not in set

# SPECIAL SET OPERATIONS (like Venn diagrams):
A = {1, 2, 3}
B = {3, 4, 5}

union = A.union(B)                          # {1,2,3,4,5} — all elements
intersection = A.intersection(B)           # {3} — common elements
difference = A.difference(B)               # {1,2} — in A but not B
sym_diff = A.symmetric_difference(B)       # {1,2,4,5} — in either but not both

# SHORTCUT OPERATORS:
# A | B   → union
# A & B   → intersection
# A - B   → difference
# A ^ B   → symmetric difference

# USE CASE FOR SET:
# Remove duplicates from a list:
nums = [1, 2, 2, 3, 3, 4]
unique = list(set(nums))   # convert list → set (removes dupes) → back to list

# INTERVIEW QUESTIONS:
# Q1: Why can't you store a list inside a set?
# A: Sets require hashable (immutable) elements
#    Lists are mutable and therefore unhashable → TypeError

# Q2: What is the difference between remove() and discard() in set?
# A: remove(x) → KeyError if x not found
#    discard(x) → No error, silently does nothing

# Q3: How do you create an empty set?
# A: s = set()  NOT s = {} (curly braces without content = empty dict!)

# Q4: Can a set contain duplicate values?
# A: No — sets automatically discard duplicates


# ============================================================
# CHAPTER 14: DICTIONARY
# ============================================================

# DICTIONARY PROPERTIES:
# Mutable        → can add, update, delete key-value pairs
# Ordered        → maintains insertion order (Python 3.7+)
# Keys unique    → duplicate keys NOT allowed (value gets overwritten)
# Values can duplicate → values can repeat
# Heterogeneous  → keys and values can be different types

# CREATE A DICTIONARY:
student = {"name": "John", "age": 20, "gpa": 9.1}
empty_dict = {}    # empty dictionary

# KEYS act like indices in list:
print(student["name"])    # "John"
print(student["age"])     # 20

# CRUD OPERATIONS:

# CREATE (add new key-value):
student["city"] = "Mumbai"

# READ (access value):
print(student["name"])          # direct access — KeyError if key missing
print(student.get("name"))      # safe access — returns None if key missing
print(student.get("phone", "N/A"))  # returns "N/A" if key missing

# UPDATE (change value):
student["age"] = 21      # key exists → updates value

# DELETE:
del student["city"]           # removes key-value pair
removed = student.pop("gpa")  # removes and returns value

# IMPORTANT NOTE ON KEYS:
# Keys are immutable after creation
# You can change VALUES but not KEYS
# To "change" a key: delete old key, add new key with same value

# DICTIONARY TRAVERSAL:
numbers = {1: 10, 2: 20, 3: 30}

# Default loop → iterates over KEYS:
for key in numbers:
    print(key, ":", numbers[key])   # key and value

# Using .items() → gives (key, value) tuples:
for key, value in numbers.items():
    print(key, "→", value)

# Using .keys():
for key in numbers.keys():
    print(key)

# Using .values():
for value in numbers.values():
    print(value)

# USEFUL DICTIONARY METHODS:
d = {"a": 1, "b": 2, "c": 3}
d.keys()     # returns all keys
d.values()   # returns all values
d.items()    # returns all (key, value) pairs
d.get("a")   # safe access
d.pop("b")   # removes and returns value of "b"
d.update({"d": 4})  # merges another dict into d
d.clear()    # removes all key-value pairs

# PRACTICE QUESTIONS (from book):
# Q1: Merge two dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
merged = {**d1, **d2}   # unpacking operator
print(merged)            # {"a":1, "b":2, "c":3, "d":4}

# Q2: Sum all values in dictionary
sales = {"jan": 100, "feb": 200, "mar": 150}
total = sum(sales.values())
print(f"Total = {total}")

# Q3: Count frequency of each element in list
items = ["apple", "banana", "apple", "cherry", "banana", "apple"]
freq = {}
for item in items:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1
print(freq)   # {"apple":3, "banana":2, "cherry":1}

# Q4: Combine two dicts — add values for common keys
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 4, "c": 1, "d": 5}
result = {}
for key in set(d1) | set(d2):
    result[key] = d1.get(key, 0) + d2.get(key, 0)
print(result)

# INTERVIEW QUESTIONS:
# Q1: What is the difference between list and dictionary?
# A: List uses integer index (0,1,2...), dict uses custom keys
#    List ordered by position, dict ordered by insertion (3.7+)

# Q2: What is the difference between dict[key] and dict.get(key)?
# A: dict[key] → raises KeyError if key doesn't exist
#    dict.get(key) → returns None (or default) if key doesn't exist

# Q3: Are dictionary keys mutable?
# A: No — keys must be immutable (strings, numbers, tuples)
#    Lists as keys → TypeError (unhashable type)

# Q4: Can two keys have the same name in a dict?
# A: No — duplicate key overwrites previous value
#    d = {"a": 1, "a": 2} → {"a": 2}


# ============================================================
# CHAPTER 15: EXCEPTION HANDLING
# ============================================================

# TYPES OF ERRORS IN PYTHON:

# 1. SYNTAX ERROR → wrong code structure — can't run at all
# print("Hello"   ← missing closing bracket
# These CANNOT be handled — must fix in code

# 2. INDENTATION ERROR → wrong indentation
# def func():
# print("hello")  ← not indented — IndentationError
# These CANNOT be handled either

# 3. EXCEPTIONS → errors that occur DURING execution (runtime errors)
# print(10 / 0)   ← ZeroDivisionError
# print("abc" + 5) ← TypeError
# These CAN be handled using try-except!

# WHAT IS AN EXCEPTION?
# An unexpected event during program execution
# Disrupts the normal flow of the program
# Example: dividing by zero, accessing invalid index, wrong type operation

# EXAMPLE WITHOUT HANDLING:
# print("Start")
# print(10 / 0)    ← ZeroDivisionError → program CRASHES here
# print("End")     ← this line NEVER runs

# EXCEPTION HANDLING KEYWORDS:
# try     → wrap code that MIGHT raise an exception
# except  → handle the exception if it occurs
# else    → runs ONLY if NO exception occurred
# finally → runs ALWAYS regardless of exception
# raise   → manually throw an exception

# BASIC SYNTAX:
try:
    result = 10 / 0          # risky code goes here
except ZeroDivisionError:
    print("Can't divide by zero!")   # handles specific exception
else:
    print("Division successful!")    # runs only if no exception
finally:
    print("This always runs!")       # cleanup code here

# CATCHING MULTIPLE EXCEPTIONS:
try:
    x = int(input("Enter number: "))
    result = 10 / x
    print(result)
except ValueError:
    print("Please enter a valid integer!")
except ZeroDivisionError:
    print("Can't divide by zero!")
except Exception as e:
    print(f"Unexpected error: {e}")    # catches any other exception

# 'Exception as e' → e contains the error message string
# Good practice: catch specific exceptions first, generic Exception last

# RAISE — manually throw exception:
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(e)   # "Age cannot be negative!"

# COMMON PYTHON EXCEPTIONS:
# ValueError          → wrong value (int("hello"))
# TypeError           → wrong type ("hello" + 5)
# ZeroDivisionError   → division by zero
# IndexError          → index out of range (lst[10] on small list)
# KeyError            → key not found in dictionary
# FileNotFoundError   → file doesn't exist
# NameError           → variable not defined
# AttributeError      → wrong method for that type

# INTERVIEW QUESTIONS:
# Q1: What is the difference between error and exception?
# A: Errors (SyntaxError, IndentationError) = code is wrong, can't run
#    Exceptions = occur at runtime, CAN be caught and handled

# Q2: What is the finally block used for?
# A: Code that MUST run regardless — typically cleanup
#    Examples: closing file, closing database connection, releasing memory

# Q3: What is the difference between except Exception and bare except?
# A: except Exception catches most exceptions (not SystemExit, KeyboardInterrupt)
#    bare except: catches EVERYTHING including system-level exceptions (bad practice)
#    Always use except Exception or specific exception types

# Q4: What does raise do?
# A: Manually triggers an exception — useful for input validation
#    Lets you create meaningful error messages for users


# ============================================================
# CHAPTER 16: FILE HANDLING
# ============================================================

# WHAT ARE FILES?
# Any file with a name + extension (.py, .txt, .mp3, .csv, etc.)
# File handling = performing CRUD operations on files
# CRUD = Create, Read, Update, Delete

# TO OPEN A FILE: use open() function
# SYNTAX: open("filename", "mode")

# FILE OPENING MODES:
# "r"  → Read (default) — file must exist, else FileNotFoundError
# "w"  → Write — creates file if not exists, OVERWRITES if exists
# "a"  → Append — adds to END of file, creates if not exists
# "x"  → Create — creates new file, ERROR if already exists

# READING A FILE:
file = open("myfile.txt", "r")
content = file.read()          # reads entire file as one string
print(content)
file.close()                   # MUST close file after use!

# read() → entire file as string
# readline() → reads ONE line (moves pointer forward)
# readlines() → reads ALL lines into a LIST

# BETTER WAY — with keyword (auto-closes file):
with open("data.txt", "r") as f:
    content = f.read()
    print(content)
# file automatically closed when 'with' block ends — even if error occurs!

# WRITING TO A FILE:
with open("output.txt", "w") as f:
    f.write("Hello World\n")
    f.write("Python is great\n")
# "w" mode → overwrites entire file if it already exists

# APPENDING TO A FILE:
with open("output.txt", "a") as f:
    f.write("New line added\n")
# "a" mode → adds to end, doesn't overwrite

# READING LINE BY LINE (memory efficient for large files):
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())   # strip() removes \n at end of each line

# FILE HANDLING PROJECT IDEA:
# Simple contact book using file handling:
# - Add contact → write to file
# - View contacts → read from file
# - This is real-world file handling!

# INTERVIEW QUESTIONS:
# Q1: What is the difference between "w" and "a" mode?
# A: "w" = write — overwrites everything, starts fresh
#    "a" = append — adds to end, preserves existing content

# Q2: Why should you always close a file?
# A: Unclosed files waste memory (file descriptor leak)
#    Data may not be saved (OS buffers writes until file is closed)
#    'with' statement handles this automatically (recommended)

# Q3: What is the advantage of using 'with' for file handling?
# A: Automatically closes file even if an exception occurs
#    Cleaner code — no need to manually call file.close()

# Q4: What happens if you open a non-existent file in "r" mode?
# A: FileNotFoundError is raised
#    Use "w" or "a" mode to create a new file


# ============================================================
# CHAPTER 17-27: OOP (OBJECT ORIENTED PROGRAMMING)
# ============================================================

# WHAT IS OOP?
# A programming PARADIGM (approach/style) based on "objects"
# Objects = entities that contain DATA (attributes) + BEHAVIOR (methods)

# 3 PARADIGMS COMPARED:
# 1. Imperative  → just variables and expressions (a = 5; print(a+b))
# 2. Functional  → functions group reusable logic
# 3. OOP         → classes and objects (most scalable for large programs)

# WHY OOP?
# Without OOP: need separate variables for every new entity
# With OOP: one class → create unlimited objects (each with own data)

# OOP 4 PILLARS:
# 1. Encapsulation  → bundling data + methods + hiding internal details
# 2. Inheritance    → child class gets properties of parent class
# 3. Polymorphism   → same method name, different behavior
# 4. Abstraction    → hide complexity, show only essentials


# ===== CLASSES =====

# CLASS = blueprint/template for creating objects
# Like a bag factory blueprint — defines what every bag must have
# Does NOT create actual bag — it's just the design

# CLASS SYNTAX:
class Car:
    brand = "Toyota"    # class attribute (shared by all objects)

# Class has 2 things:
# Attributes = variables defined inside class (data)
# Methods    = functions defined inside class (behavior)

class Animal:
    species = "Dog"        # Attribute

    def make_sound(self):  # Method
        print("Bark!")

# ACCESSING WITHOUT OBJECT (directly via class):
print(Animal().species)    # "Dog"
Animal().make_sound()      # "Bark!"


# ===== OBJECTS =====

# OBJECT = actual instance created FROM a class
# Like actual bags made using the factory blueprint
# Each object has its own copy of instance attributes

class Fruit:
    name = "Apple"

f = Fruit()           # f is the OBJECT (instance)
print(f.name)         # "Apple" — accessing attribute via object

# Multiple objects from same class:
f1 = Fruit()
f2 = Fruit()
# f1 and f2 are separate objects in different memory locations


# ===== CONSTRUCTOR (__init__) =====

# WHAT IS A CONSTRUCTOR?
# Special method that runs AUTOMATICALLY when object is created
# Used to initialize instance attributes with values
# In Python: def __init__(self, ...)

# 'self' = refers to the CURRENT OBJECT being created
# self is why each object gets its own copy of attributes

class Student:
    def __init__(self, name, age):
        self.name = name    # instance attribute
        self.age = age      # instance attribute

# Creating objects with values:
s1 = Student("Riya", 20)    # __init__ called with name="Riya", age=20
s2 = Student("Arjun", 22)   # __init__ called with name="Arjun", age=22

print(s1.name)   # "Riya"
print(s2.name)   # "Arjun"
# s1 and s2 have DIFFERENT name and age — because self targets each object


# ===== TYPES OF ATTRIBUTES =====

# 1. CLASS ATTRIBUTE: defined directly inside class (outside methods)
#    Shared by ALL objects of that class

# 2. INSTANCE ATTRIBUTE: defined using self inside __init__
#    Each object has its OWN copy

class Car:
    wheels = 4             # CLASS attribute — same for all cars

    def __init__(self, color):
        self.color = color  # INSTANCE attribute — different per car

c1 = Car("Red")
c2 = Car("Blue")
print(c1.wheels)   # 4 (class attribute)
print(c2.wheels)   # 4 (same class attribute)
print(c1.color)    # "Red" (instance attribute)
print(c2.color)    # "Blue" (different instance attribute)


# ===== TYPES OF METHODS =====

# 1. INSTANCE METHOD: most common — works with object (self)
class MyClass:
    def instance_method(self):
        print("Instance method — accesses self/object")

# 2. CLASS METHOD: works with class itself, not object
#    Use @classmethod decorator + cls parameter
class MyClass:
    count = 0

    @classmethod
    def class_method(cls):
        cls.count += 1
        print(f"Class method — count = {cls.count}")

# 3. STATIC METHOD: no access to self or cls
#    Like a regular function placed inside a class
#    Use @staticmethod decorator
class MyClass:
    @staticmethod
    def static_method():
        print("Static method — no self, no cls")

# DECORATOR = @ symbol before function
# Modifies behavior of the function
# @classmethod and @staticmethod are built-in decorators


# ===== INHERITANCE =====

# WHAT IS INHERITANCE?
# Child class inherits attributes and methods from parent class
# Child gets everything parent has + can add its own stuff
# Benefits: code reuse, organized structure, easy to extend

# SYNTAX: class Child(Parent):
class Parent:
    def speak(self):
        print("I can speak!")

class Child(Parent):
    pass    # Child has nothing extra, but inherits speak()

c = Child()
c.speak()    # works! inherited from Parent

# CONSTRUCTOR IN INHERITANCE:
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def display(self):
        print(f"My name is {self.name}")   # can access parent's attribute

c = Child("Riya")    # uses Parent's __init__ automatically
c.display()          # "My name is Riya"

# super() — call parent's constructor from child:
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)    # calls Parent.__init__(name)
        self.age = age            # add child's own attribute

    def display(self):
        print(f"My name is {self.name}, I am {self.age}")

c = Child("John", 20)
c.display()    # "My name is John, I am 20"

# TYPES OF INHERITANCE:
# 1. Single Inheritance → one parent, one child
# 2. Multiple Inheritance → two parents, one child
# 3. Multilevel Inheritance → grandparent → parent → child

# Multiple Inheritance:
class Father:
    def skills(self): print("Coding")

class Mother:
    def skills(self): print("Cooking")

class Child(Father, Mother):
    def show(self): print("I have multiple skills")

c = Child()
c.skills()    # "Coding" — Father's skills() because Father listed first (MRO)

# MRO = Method Resolution Order
# Python follows left-to-right order in multiple inheritance
# Use ClassName.__mro__ to see the order

# Multilevel Inheritance:
class Grandparent:
    def heritage(self): print("Heritage from Grandparent")

class Parent(Grandparent): pass

class Child(Parent): pass

c = Child()
c.heritage()  # works! inherited through Parent from Grandparent


# ===== POLYMORPHISM =====

# WHAT IS POLYMORPHISM?
# "poly" = many, "morphism" = forms
# Same method name behaves differently depending on the object

# Python achieves polymorphism in 2 ways:
# 1. Method Overriding (runtime polymorphism)
# 2. Duck Typing

# Note: Python does NOT support Method Overloading
# Method Overloading = same name, different parameters → Python overwrites!
# def add(a): pass
# def add(a, b): pass   ← this REPLACES the first add

# 1. METHOD OVERRIDING:
# Child class provides its own implementation of parent's method
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):      # overrides parent's sound()
        print("Dog barks")

class Cat(Animal):
    def sound(self):      # overrides parent's sound()
        print("Cat meows")

animals = [Dog(), Cat()]
for a in animals:
    a.sound()   # Dog barks, Cat meows — same method, different behavior

# 2. DUCK TYPING:
# "If it walks like a duck and quacks like a duck, it's a duck"
# Python doesn't care about TYPE — only cares about METHOD NAME
class Duck:
    def talk(self): print("Quack!")

class Human:
    def talk(self): print("Hello!")

def make_talk(obj):
    obj.talk()    # doesn't care if it's Duck or Human — just needs talk()

make_talk(Duck())   # Quack!
make_talk(Human())  # Hello!


# ===== ENCAPSULATION =====

# WHAT IS ENCAPSULATION?
# 1. Bundling data (attributes) + behavior (methods) into one class
# 2. Hiding internal details (access control)
# Benefits: data safety, clean code, controlled access

# ACCESS MODIFIERS IN PYTHON (3 types):

# 1. PUBLIC: default — accessible everywhere
self.name = "Public"          # no prefix

# 2. PROTECTED: single underscore prefix _
self._age = 21                # convention: "don't access outside class"
# Python doesn't enforce this — it's just a WARNING to other developers

# 3. PRIVATE: double underscore prefix __
self.__salary = 50000         # truly restricted — name mangling applied
# obj.__salary → AttributeError!
# Actual name becomes: obj._ClassName__salary (name mangling)

class Demo:
    def __init__(self):
        self.name = "Public Member"       # public
        self._age = 21                    # protected
        self.__salary = 50000             # private

    def show(self):
        print(self.name)       # accessible inside class ✅
        print(self._age)       # accessible inside class ✅
        print(self.__salary)   # accessible inside class ✅

d = Demo()
d.show()              # works — accessing via method (correct way)
print(d.name)         # works — public
print(d._age)         # works — but convention says don't
# print(d.__salary)   # AttributeError — private!
print(d._Demo__salary) # works — name mangling bypass (not recommended)


# ===== ABSTRACTION =====

# WHAT IS ABSTRACTION?
# Hiding complex implementation — showing only essential features
# Defines WHAT a class must do — not HOW it does it
# Python achieves abstraction using ABC (Abstract Base Class) from abc module

from abc import ABC, abstractmethod

class Animal(ABC):    # Abstract class
    @abstractmethod
    def make_sound(self):    # Abstract method — no implementation
        pass

class Dog(Animal):
    def make_sound(self):    # MUST implement abstract method
        print("Dog says Woof!")

class Cat(Animal):
    def make_sound(self):    # MUST implement abstract method
        print("Cat says Meow!")

# d = Animal()   ← TypeError! Can't instantiate abstract class
d = Dog()        # works — Dog implements all abstract methods
d.make_sound()   # "Dog says Woof!"

# WHY ABSTRACTION?
# Forces subclasses to implement required methods
# Creates a "contract" — all subclasses must follow the same interface
# Used heavily in frameworks and APIs


# ===== DUNDER (MAGIC) METHODS =====

# WHAT ARE DUNDER METHODS?
# Special methods with double underscore prefix AND suffix
# Format: __methodname__
# Called AUTOMATICALLY when certain operations are performed on objects
# Examples: __init__, __str__, __add__, __len__, __eq__

# __init__ → called when object created (constructor)
# __str__ → called when print(object) is used
# __add__ → called when + operator used on objects
# __len__ → called when len(object) is used
# __eq__  → called when == used on objects

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}"

    def __add__(self, other):
        return Person(self.name + " & " + other.name, self.age + other.age)

    def __eq__(self, other):
        return self.age == other.age

p1 = Person("Ravi", 20)
p2 = Person("Priya", 20)

print(p1)           # calls __str__ → "Person: Ravi, Age: 20"
p3 = p1 + p2        # calls __add__
print(p1 == p2)     # calls __eq__ → True (both age 20)


# ===== ADVANCED: DECORATOR =====

# WHAT IS A DECORATOR?
# A function that MODIFIES another function without changing its code
# Like icing on a cake — doesn't change the cake, just adds something

# HOW IT WORKS:
# 1. Create decorator function (takes a function as input)
# 2. Inside, create wrapper function (adds extra behavior)
# 3. Return wrapper
# 4. Apply using @decorator_name before target function

def my_decorator(func):
    def wrapper():
        print("Something before the function runs.")
        func()
        print("Something after the function runs.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something before the function runs.
# Hello!
# Something after the function runs.

# @my_decorator is same as: say_hello = my_decorator(say_hello)


# ===== ADVANCED: *ARGS AND **KWARGS =====

# *args   → accept UNLIMITED positional arguments (stored as TUPLE)
# **kwargs → accept UNLIMITED keyword arguments (stored as DICT)

def fun(*args, **kwargs):
    print("Args:", args)     # tuple of positional args
    print("Kwargs:", kwargs) # dict of keyword args

fun(1, 2, 3, name="Arin", age=21)
# Args: (1, 2, 3)
# Kwargs: {'name': 'Arin', 'age': 21}

# The * and ** are what matter — not the names args/kwargs
# def func(*numbers, **data): works the same way


# ===== ADVANCED: COMPREHENSIONS =====

# List, Dict, Set comprehensions = shorter way to create them
# Instead of for loop + append, write in one line

# LIST COMPREHENSION:
# [expression for item in iterable if condition]
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
# ['Even', 'Odd', 'Even', 'Odd', 'Even']

squares = [x**2 for x in range(1, 6)]
# [1, 4, 9, 16, 25]

# DICT COMPREHENSION:
evens = {x: x*x for x in range(10) if x % 2 == 0}
# {0:0, 2:4, 4:16, 6:36, 8:64}

# SET COMPREHENSION:
unique_even_sq = {x*x for x in range(10) if x % 2 == 0}
# {0, 4, 16, 36, 64}


# ===== ADVANCED: LAMBDA FUNCTIONS =====

# WHAT IS LAMBDA?
# Anonymous (no name) inline function
# Used for short, simple, one-time functions
# SYNTAX: lambda arguments: expression

square = lambda x: x**2
print(square(4))   # 16

add = lambda a, b: a + b
print(add(3, 5))   # 8

# With if-else:
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(7))   # "Odd"

# Common use: with map() and filter()
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))    # [2, 4, 6, 8, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

# MAP: applies function to every element → returns new iterable
# FILTER: keeps elements where function returns True → returns new iterable


# ===== ADVANCED: MODULES AND PACKAGES =====

# MODULE = single .py file containing code (functions, variables, classes)
# PACKAGE = folder containing multiple modules (+ __init__.py file)

# IMPORT A MODULE:
import math
print(math.sqrt(16))    # 4.0
print(math.pi)          # 3.14159...
print(math.floor(9.9))  # 9

import random
print(random.randint(1, 100))  # random number between 1 and 100

import datetime
print(datetime.date.today())   # today's date

# IMPORT SPECIFIC THINGS:
from math import sqrt, pi
print(sqrt(25))  # no need for math.sqrt()

# IMPORT WITH ALIAS:
import numpy as np    # np is shorter alias (common in data science)

# THIRD PARTY PACKAGES (install using pip):
# pip install numpy
# pip install pandas
# pip install matplotlib
# These are NOT built-in — must install separately

# CREATING YOUR OWN MODULE:
# Just create a .py file and import it in another .py file

# INTERVIEW QUESTIONS (OOP):
# Q1: What are the 4 pillars of OOP?
# A: Encapsulation, Inheritance, Polymorphism, Abstraction

# Q2: What is the difference between class and object?
# A: Class = blueprint (template), Object = instance (actual thing)
#    Class: Car, Object: my_car = Car()

# Q3: What is self in Python?
# A: Reference to current object (instance)
#    Allows each object to store its own attribute values separately

# Q4: What is __init__?
# A: Constructor — runs automatically when object is created
#    Used to initialize instance attributes

# Q5: What is the difference between class attribute and instance attribute?
# A: Class attribute = shared by all objects, defined outside methods
#    Instance attribute = unique per object, defined using self in __init__

# Q6: What is method overriding vs method overloading?
# A: Overriding = child class redefines parent's method (Python supports)
#    Overloading = same method name, different parameters (Python does NOT support)

# Q7: What is super()?
# A: Calls parent class method/constructor from child class
#    Used in inheritance to extend (not replace) parent functionality

# Q8: What is name mangling in Python?
# A: Double underscore (__) prefix causes Python to rename attribute
#    __salary becomes _ClassName__salary internally
#    This is how Python implements "private" access


# ============================================================
# PHASE 1 COMPLETE — WHAT'S NEXT?
# ============================================================

# ✅ You have covered:
# Installation & Setup
# Comments & Variables
# Data Types (int, float, complex, string, bool)
# Strings (indexing, slicing, type conversion)
# Input & Output (print, input, f-strings)
# Operators (arithmetic, assignment, comparison, logical)
# Conditional Statements (if, elif, else, ladder)
# Loops (for, while, break, continue, else)
# Functions (def, parameters, arguments, return)
# Data Structures (list, tuple, set, dictionary)
# Exception Handling (try, except, else, finally, raise)
# File Handling (read, write, append, with statement)
# OOP (class, object, constructor, attributes, methods)
# Inheritance (single, multiple, multilevel, super)
# Polymorphism (overriding, duck typing)
# Encapsulation (public, protected, private)
# Abstraction (ABC, abstractmethod)
# Dunder/Magic Methods
# Advanced: Decorators, *args/**kwargs, Comprehensions, Lambda, Modules

# 🔜 PHASE 2: NumPy
# Arrays, vectorization, broadcasting
# Foundation for all data science in Python

# FINAL TIPS:
# ✅ Practice every question in VS Code — don't just read
# ✅ Understand WHY — don't memorize syntax
# ✅ Build small projects (calculator, contact book, guessing game)
# ✅ Strong Python foundation = faster ML learning 