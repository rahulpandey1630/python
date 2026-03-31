# ============================================================
# ALL QUESTIONS + SOLUTIONS — PHASE 1 PYTHON
# Sheryians Coding School
# ============================================================


# ============================================================
# SECTION 1: VARIABLES & DATA TYPES QUESTIONS
# ============================================================

# Q1: Create variables for your name, age, city, gpa, is_employed
# and print all of them using f-string

name = "Akarsh"
age = 21
city = "Mumbai"
gpa = 9.2
is_employed = False

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"GPA: {gpa}")
print(f"Employed: {is_employed}")

# OUTPUT:
# Name: Akarsh
# Age: 21
# City: Mumbai
# GPA: 9.2
# Employed: False


# ============================================================

# Q2: Check type of: 5, 5.0, "5", True, 5+3j

print(type(5))      # <class 'int'>
print(type(5.0))    # <class 'float'>
print(type("5"))    # <class 'str'>
print(type(True))   # <class 'bool'>
print(type(5+3j))   # <class 'complex'>


# ============================================================

# Q3: Find unicode of first letter of your name
# and convert it back

name = "Akarsh"
first_letter = name[0]
unicode_val = ord(first_letter)
back_to_char = chr(unicode_val)

print(f"First letter: {first_letter}")
print(f"Unicode value: {unicode_val}")
print(f"Back to character: {back_to_char}")

# OUTPUT:
# First letter: A
# Unicode value: 65
# Back to character: A


# ============================================================

# Q4: Check bool() for all 7 falsy values

print(bool(0))       # False
print(bool(0.0))     # False
print(bool(False))   # False
print(bool(""))      # False
print(bool([]))      # False
print(bool({}))      # False
print(bool(()))      # False

# All non-falsy (truthy):
print(bool(1))       # True
print(bool("hi"))    # True
print(bool([1,2]))   # True
print(bool(-1))      # True  (negative numbers are truthy!)


# ============================================================

# Q5: Predict and verify: print(True + True + False + True)

result = True + True + False + True
print(result)
# True=1, True=1, False=0, True=1
# 1 + 1 + 0 + 1 = 3
# OUTPUT: 3


# ============================================================
# SECTION 2: STRING QUESTIONS
# ============================================================

# Q6: String indexing — access first, last, middle character

s = "Python"
print(s[0])      # P  (first)
print(s[-1])     # n  (last)
print(s[3])      # h  (middle-ish)
print(s[-3])     # h  (negative index from end)

# OUTPUT:
# P
# n
# h
# h


# ============================================================

# Q7: String slicing — extract different parts

s = "Hello World"

print(s[0:5])      # Hello   (index 0,1,2,3,4)
print(s[6:11])     # World   (index 6,7,8,9,10)
print(s[::2])      # HloWrd  (every 2nd character)
print(s[::-1])     # dlroW olleH  (reverse the string)
print(s[2:8:2])    # loW    (start=2, stop=8, step=2)

# OUTPUT:
# Hello
# World
# HloWrd
# dlroW olleH
# loW


# ============================================================

# Q8: Reverse a string using slicing (interview classic)

s = input("Enter a string: ")
reversed_s = s[::-1]
print(f"Reversed: {reversed_s}")

# INPUT: "Python"
# OUTPUT: nohtyP


# ============================================================
# SECTION 3: TYPE CONVERSION QUESTIONS
# ============================================================

# Q9: Accept age from user and print "You are X years old"
# (demonstrates why we need int conversion)

age = int(input("Enter your age: "))
print(f"You are {age} years old")

# Without int() → age would be string "21"
# f"You are {age} years old" would still work for printing
# BUT age + 1 would FAIL without int()
print(f"Next year you will be {age + 1}")

# INPUT: 21
# OUTPUT:
# You are 21 years old
# Next year you will be 22


# ============================================================

# Q10: Accept two numbers from user and print their sum
# (why do you need int()?)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
total = num1 + num2
print(f"Sum = {total}")

# WITHOUT int(): input returns strings
# "5" + "3" = "53"  (string concatenation, NOT addition!)
# WITH int(): 5 + 3 = 8 (actual math)

# INPUT: 5, 3
# OUTPUT: Sum = 8


# ============================================================

# Q11: Predict output of int() and float() on booleans

print(int(True))     # 1  (True = 1)
print(int(False))    # 0  (False = 0)
print(float(True))   # 1.0
print(float(False))  # 0.0
print(str(True))     # "True"
print(bool(0))       # False
print(bool(1))       # True
print(bool(99))      # True  (any non-zero = True)


# ============================================================

# Q12: Try int("hello") — understand the error

try:
    result = int("hello")
except ValueError as e:
    print(f"Error: {e}")
# Output: Error: invalid literal for int() with base 10: 'hello'

# int() can only convert:
# Strings that look like numbers: "42", "-5", "0"
# Booleans: True→1, False→0
# Floats (truncates): 9.9→9
# CANNOT convert: "hello", "12.5" (use float("12.5") first)


# ============================================================
# SECTION 4: OPERATORS QUESTIONS
# ============================================================

# Q13: Trivial Questions from book — predict before running

# Q13a: Print(126 > 130)
print(126 > 130)
# 126 is NOT greater than 130
# OUTPUT: False


# Q13b: print((456 == 456) != (235 == 236))
# Step 1: 456 == 456 → True
# Step 2: 235 == 236 → False
# Step 3: True != False → True (they ARE not equal to each other)
print((456 == 456) != (235 == 236))
# OUTPUT: True


# Q13c: print(12 < 10 or 45 == 56 or 69 > 70 or 15 != 13)
# Step 1: 12 < 10   → False
# Step 2: 45 == 56  → False
# Step 3: 69 > 70   → False
# Step 4: 15 != 13  → True
# False or False or False or True → True
# (or returns True if AT LEAST ONE is True)
print(12 < 10 or 45 == 56 or 69 > 70 or 15 != 13)
# OUTPUT: True


# Q13d: print(True and bool(0))
# Step 1: bool(0) → False
# Step 2: True and False → False
# (and returns True only if BOTH are True)
print(True and bool(0))
# OUTPUT: False


# ============================================================

# Q14: Write expression to check if number is between 10 and 20

num = int(input("Enter number: "))
if num >= 10 and num <= 20:
    print(f"{num} is between 10 and 20")
else:
    print(f"{num} is NOT between 10 and 20")

# Shorter Pythonic way:
if 10 <= num <= 20:     # chained comparison — only in Python!
    print("In range")

# INPUT: 15
# OUTPUT: 15 is between 10 and 20


# ============================================================

# Q15: Check if a string is NOT empty

s = input("Enter string: ")
if s:               # empty string is falsy, non-empty is truthy
    print("String is NOT empty")
else:
    print("String IS empty")

# Alternative explicit way:
if len(s) != 0:
    print("Not empty")

# INPUT: "hello"
# OUTPUT: String is NOT empty


# ============================================================
# SECTION 5: CONDITIONAL STATEMENTS QUESTIONS
# ============================================================

# Q16: Accept two numbers — print the greater one

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(f"{a} is greater")
elif b > a:
    print(f"{b} is greater")
else:
    print("Both numbers are equal")

# INPUT: 15, 8
# OUTPUT: 15 is greater


# ============================================================

# Q17: Accept gender as char — print greeting message

gender = input("Enter gender (M/F): ")

if gender == "M" or gender == "m":
    print("Good Morning Sir")
elif gender == "F" or gender == "f":
    print("Good Morning Ma'am")
else:
    print("Invalid input! Please enter M or F")

# INPUT: M
# OUTPUT: Good Morning Sir


# ============================================================

# Q18: Accept integer — check even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# LOGIC: if number divided by 2 has remainder 0 → even
# INPUT: 7
# OUTPUT: 7 is Odd


# ============================================================

# Q19: Accept name and age — check valid voter

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"Hello {name}, you are a valid voter")
else:
    print(f"Hello {name}, you are NOT a valid voter yet")
    years_left = 18 - age
    print(f"You need {years_left} more year(s) to be eligible")

# INPUT: Akarsh, 21
# OUTPUT: Hello Akarsh, you are a valid voter


# ============================================================

# Q20: Accept year — check leap year or not

year = int(input("Enter a year: "))

# LEAP YEAR RULES:
# Rule 1: divisible by 4 → potential leap year
# Rule 2: BUT if divisible by 100 → NOT a leap year
# Rule 3: UNLESS also divisible by 400 → IS a leap year
# Combined: (div by 4 AND not div by 100) OR (div by 400)

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is NOT a Leap Year")

# TEST CASES:
# 2000 → Leap (div by 400)
# 1900 → NOT Leap (div by 100 but not 400)
# 2024 → Leap (div by 4, not by 100)
# 2023 → NOT Leap


# ============================================================

# Q21: Temperature if-elif ladder

temp = float(input("Enter temperature in Celsius: "))

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

# INPUT: 25
# OUTPUT: Pleasant ☁️


# ============================================================
# SECTION 6: FOR LOOP QUESTIONS
# ============================================================

# Q22: Accept n — print "hello world" n times

n = int(input("Enter n: "))
for i in range(n):
    print("hello world")

# INPUT: 3
# OUTPUT:
# hello world
# hello world
# hello world


# ============================================================

# Q23: Print natural numbers from 1 to n

n = int(input("Enter n: "))
for i in range(1, n + 1):
    print(i)

# INPUT: 5
# OUTPUT: 1 2 3 4 5 (each on new line)


# ============================================================

# Q24: Reverse for loop — print n to 1

n = int(input("Enter n: "))
for i in range(n, 0, -1):
    print(i)

# range(n, 0, -1) → starts at n, goes down by 1, stops before 0
# INPUT: 5
# OUTPUT: 5 4 3 2 1 (each on new line)


# ============================================================

# Q25: Take number as input — print its multiplication table

num = int(input("Enter a number: "))
print(f"\nMultiplication Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# INPUT: 5
# OUTPUT:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50


# ============================================================

# Q26: Sum up to n terms (1 + 2 + 3 + ... + n)

n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum of 1 to {n} = {total}")

# BONUS: Formula approach (no loop needed)
formula_result = n * (n + 1) // 2
print(f"Using formula: {formula_result}")

# INPUT: 5
# OUTPUT: Sum of 1 to 5 = 15


# ============================================================

# Q27: Factorial of a number

n = int(input("Enter n: "))
factorial = 1

if n < 0:
    print("Factorial not defined for negative numbers")
elif n == 0:
    print("0! = 1")
else:
    for i in range(1, n + 1):
        factorial *= i
    print(f"{n}! = {factorial}")

# INPUT: 5
# OUTPUT: 5! = 120
# LOGIC: 5! = 5 × 4 × 3 × 2 × 1 = 120


# ============================================================

# Q28: Print sum of all even and odd numbers in range separately

n = int(input("Enter n: "))
even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f"Sum of even numbers (1 to {n}): {even_sum}")
print(f"Sum of odd numbers (1 to {n}): {odd_sum}")

# INPUT: 10
# OUTPUT:
# Sum of even numbers: 30  (2+4+6+8+10)
# Sum of odd numbers: 25   (1+3+5+7+9)


# ============================================================

# Q29: Print all factors of a number

n = int(input("Enter a number: "))
print(f"Factors of {n}:")

for i in range(1, n + 1):
    if n % i == 0:
        print(i)

# INPUT: 12
# OUTPUT: 1 2 3 4 6 12


# ============================================================

# Q30: Check if number is perfect number
# Perfect number = sum of all factors (excluding itself) = number
# Example: 6 → factors: 1,2,3 → 1+2+3=6 ✅

n = int(input("Enter a number: "))
factor_sum = 0

for i in range(1, n):    # range(1, n) → excludes n itself
    if n % i == 0:
        factor_sum += i

if factor_sum == n:
    print(f"{n} is a Perfect Number ✅")
else:
    print(f"{n} is NOT a Perfect Number ❌")
    print(f"Sum of factors = {factor_sum}")

# INPUT: 6
# OUTPUT: 6 is a Perfect Number ✅
# OTHER PERFECT NUMBERS: 28, 496, 8128


# ============================================================

# Q31: Check if number is prime or not

n = int(input("Enter a number: "))
is_prime = True

if n < 2:
    is_prime = False
else:
    # Optimized: only check up to square root of n
    # If n has factor > sqrt(n), other factor must be < sqrt(n)
    # So we would have already found it
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{n} is a Prime Number ✅")
else:
    print(f"{n} is NOT a Prime Number ❌")

# INPUT: 17
# OUTPUT: 17 is a Prime Number ✅
# INPUT: 15
# OUTPUT: 15 is NOT a Prime Number (15 = 3 × 5)


# ============================================================

# Q32: Reverse a string WITHOUT using built-in functions

s = input("Enter a string: ")
reversed_s = ""

for i in range(len(s) - 1, -1, -1):
    reversed_s += s[i]

print(f"Original : {s}")
print(f"Reversed : {reversed_s}")

# range(len(s)-1, -1, -1):
# Start at last index, go backwards, stop before -1 (i.e., stop at 0)
# INPUT: "Python"
# OUTPUT: nohtyP


# ============================================================

# Q33: Check if string is Palindrome
# Palindrome = reads same forwards and backwards
# Examples: "madam", "racecar", "level"

s = input("Enter a string: ")
s_lower = s.lower()   # make case-insensitive

if s_lower == s_lower[::-1]:
    print(f'"{s}" is a Palindrome ✅')
else:
    print(f'"{s}" is NOT a Palindrome ❌')

# INPUT: "madam"
# OUTPUT: "madam" is a Palindrome ✅
# INPUT: "Python"
# OUTPUT: "Python" is NOT a Palindrome ❌


# ============================================================

# Q34: Count all letters, digits, and special symbols in a string

s = "P@#yn26at^&i5ve"
letters = 0
digits = 0
symbols = 0

for char in s:
    if char.isalpha():    # isalpha() → True if letter (a-z, A-Z)
        letters += 1
    elif char.isdigit():  # isdigit() → True if digit (0-9)
        digits += 1
    else:
        symbols += 1      # anything else is special symbol

print(f"String: {s}")
print(f"Letters = {letters}")
print(f"Digits  = {digits}")
print(f"Symbols = {symbols}")

# OUTPUT:
# Letters = 8
# Digits  = 3
# Symbols = 4


# ============================================================
# SECTION 7: WHILE LOOP QUESTIONS
# ============================================================

# Q35: Separate each digit of a number and print on new line

n = int(input("Enter a number: "))
print(f"Digits of {n}:")

original = n
digits_list = []

while n > 0:
    digit = n % 10        # extract last digit
    digits_list.append(digit)
    n = n // 10           # remove last digit

# digits are in reverse order, print them correctly
digits_list.reverse()
for d in digits_list:
    print(d)

# INPUT: 1234
# OUTPUT: 1 2 3 4
# LOGIC:
# 1234 % 10 = 4, 1234 // 10 = 123
# 123  % 10 = 3, 123  // 10 = 12
# 12   % 10 = 2, 12   // 10 = 1
# 1    % 10 = 1, 1    // 10 = 0 → loop ends


# ============================================================

# Q36: Accept a number — print its reverse

n = int(input("Enter a number: "))
original = n
reversed_n = 0

while n > 0:
    digit = n % 10
    reversed_n = reversed_n * 10 + digit
    n = n // 10

print(f"Original : {original}")
print(f"Reversed : {reversed_n}")

# INPUT: 1234
# STEP BY STEP:
# reversed=0,  digit=4, reversed = 0*10+4 = 4,    n=123
# reversed=4,  digit=3, reversed = 4*10+3 = 43,   n=12
# reversed=43, digit=2, reversed = 43*10+2 = 432, n=1
# reversed=432,digit=1, reversed = 432*10+1=4321, n=0
# OUTPUT: 4321


# ============================================================

# Q37: Check if a number is a palindrome number

n = int(input("Enter a number: "))
original = n
reversed_n = 0

while n > 0:
    digit = n % 10
    reversed_n = reversed_n * 10 + digit
    n = n // 10

if original == reversed_n:
    print(f"{original} is a Palindrome Number ✅")
else:
    print(f"{original} is NOT a Palindrome Number ❌")

# INPUT: 121
# OUTPUT: 121 is a Palindrome Number ✅
# INPUT: 123
# OUTPUT: 123 is NOT a Palindrome Number ❌


# ============================================================

# Q38: Create a random number guessing game

import random

secret = random.randint(1, 100)
guess = 0
attempts = 0
max_attempts = 7

print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between 1 and 100")
print(f"You have {max_attempts} attempts\n")

while guess != secret and attempts < max_attempts:
    guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
    attempts += 1

    if guess < secret:
        remaining = max_attempts - attempts
        print(f"Too LOW! {remaining} attempts remaining\n")
    elif guess > secret:
        remaining = max_attempts - attempts
        print(f"Too HIGH! {remaining} attempts remaining\n")
    else:
        print(f"🎉 CORRECT! The number was {secret}")
        print(f"You got it in {attempts} attempt(s)!")

if guess != secret:
    print(f"Game Over! The number was {secret}")


# ============================================================
# SECTION 8: FUNCTIONS QUESTIONS
# ============================================================

# Q39: Function to check even or odd

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter number: "))
result = check_even_odd(num)
print(f"{num} is {result}")

# INPUT: 8
# OUTPUT: 8 is Even


# ============================================================

# Q40: Function to find factorial

def factorial(n):
    if n < 0:
        return "Not defined"
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input("Enter n: "))
print(f"{n}! = {factorial(n)}")

# INPUT: 6
# OUTPUT: 6! = 720


# ============================================================

# Q41: Function to check prime

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter number: "))
if is_prime(num):
    print(f"{num} is Prime ✅")
else:
    print(f"{num} is Not Prime ❌")


# ============================================================

# Q42: Function with default argument — greet

def greet(name="Guest", greeting="Hello"):
    print(f"{greeting}, {name}! Welcome to Python.")

greet()                          # uses both defaults
greet("Akarsh")                  # overrides name only
greet("Riya", "Good Morning")    # overrides both
greet(greeting="Hi", name="Bob") # keyword arguments

# OUTPUT:
# Hello, Guest! Welcome to Python.
# Hello, Akarsh! Welcome to Python.
# Good Morning, Riya! Welcome to Python.
# Hi, Bob! Welcome to Python.


# ============================================================

# Q43: Function that returns multiple values

def get_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    return total, average, minimum, maximum   # returns tuple

nums = [10, 20, 30, 40, 50]
total, avg, mini, maxi = get_stats(nums)

print(f"Total   : {total}")
print(f"Average : {avg}")
print(f"Minimum : {mini}")
print(f"Maximum : {maxi}")

# OUTPUT:
# Total   : 150
# Average : 30.0
# Minimum : 10
# Maximum : 50


# ============================================================

# Q44: Function using *args (unlimited positional arguments)

def add_all(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(add_all(1, 2))           # 3
print(add_all(1, 2, 3, 4, 5))  # 15
print(add_all(10, 20, 30))     # 60

# *numbers becomes a TUPLE: (1, 2, 3, 4, 5)


# ============================================================

# Q45: Function using **kwargs (unlimited keyword arguments)

def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_info(name="Akarsh", age=21, city="Mumbai", gpa=9.2)

# OUTPUT:
# name: Akarsh
# age: 21
# city: Mumbai
# gpa: 9.2
# **details becomes a DICT: {'name':'Akarsh', 'age':21, ...}


# ============================================================
# SECTION 9: LIST QUESTIONS
# ============================================================

# Q46: Print positive and negative elements of a list separately

nums = [3, -1, 7, -4, 2, -8, 5, -3, 9]
positive = []
negative = []

for n in nums:
    if n > 0:
        positive.append(n)
    elif n < 0:
        negative.append(n)

print(f"Positive numbers: {positive}")
print(f"Negative numbers: {negative}")

# OUTPUT:
# Positive numbers: [3, 7, 2, 5, 9]
# Negative numbers: [-1, -4, -8, -3]


# ============================================================

# Q47: Find mean (average) of list elements

nums = [10, 20, 30, 40, 50]

# Method 1: manual
total = 0
for n in nums:
    total += n
mean = total / len(nums)
print(f"Mean (manual): {mean}")

# Method 2: using built-in functions
mean2 = sum(nums) / len(nums)
print(f"Mean (built-in): {mean2}")

# OUTPUT: 30.0


# ============================================================

# Q48: Find greatest element and print its index too

nums = [3, 7, 1, 9, 4, 9, 2]

max_val = max(nums)
max_idx = nums.index(max_val)   # index() gives FIRST occurrence

print(f"Greatest element: {max_val}")
print(f"Found at index: {max_idx}")

# Manual way (without max()):
max_manual = nums[0]
max_manual_idx = 0
for i in range(len(nums)):
    if nums[i] > max_manual:
        max_manual = nums[i]
        max_manual_idx = i

print(f"Greatest (manual): {max_manual} at index {max_manual_idx}")

# OUTPUT:
# Greatest element: 9
# Found at index: 3


# ============================================================

# Q49: Find second greatest element

nums = [3, 7, 1, 9, 4, 6, 2]

# Method 1: sort and get second last
sorted_unique = sorted(set(nums), reverse=True)
# set() removes duplicates, sorted() sorts, reverse=True descending
print(f"Second greatest: {sorted_unique[1]}")

# Method 2: manual without sorting
first = float('-inf')   # negative infinity
second = float('-inf')

for n in nums:
    if n > first:
        second = first
        first = n
    elif n > second and n != first:
        second = n

print(f"Second greatest (manual): {second}")

# OUTPUT: 7


# ============================================================

# Q50: Check if list is sorted or not

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 3, 2, 5, 4]

# Method 1: compare with sorted version
def is_sorted(lst):
    return lst == sorted(lst)

print(f"nums1 sorted: {is_sorted(nums1)}")   # True
print(f"nums2 sorted: {is_sorted(nums2)}")   # False

# Method 2: check each consecutive pair
def is_sorted_manual(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

print(f"nums1 sorted (manual): {is_sorted_manual(nums1)}")  # True
print(f"nums2 sorted (manual): {is_sorted_manual(nums2)}")  # False


# ============================================================
# SECTION 10: DICTIONARY QUESTIONS
# ============================================================

# Q51: Merge two Python dictionaries

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"d": 4, "e": 5, "f": 6}

# Method 1: ** unpacking operator
merged1 = {**d1, **d2}
print(f"Merged (unpacking): {merged1}")

# Method 2: update()
merged2 = d1.copy()
merged2.update(d2)
print(f"Merged (update): {merged2}")

# Method 3: | operator (Python 3.9+)
merged3 = d1 | d2
print(f"Merged (| operator): {merged3}")

# OUTPUT: {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}


# ============================================================

# Q52: Sum all values in a dictionary

sales = {"jan": 1000, "feb": 1500, "mar": 1200, "apr": 1800}

# Method 1: sum() with .values()
total = sum(sales.values())
print(f"Total sales: {total}")

# Method 2: manual loop
total_manual = 0
for value in sales.values():
    total_manual += value
print(f"Total sales (manual): {total_manual}")

# OUTPUT: 5500


# ============================================================

# Q53: Count frequency of each element in a list

items = ["apple", "banana", "apple", "cherry", "banana", "apple", "mango"]
freq = {}

for item in items:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print("Frequency count:")
for item, count in freq.items():
    print(f"  {item}: {count}")

# Shorter using .get():
freq2 = {}
for item in items:
    freq2[item] = freq2.get(item, 0) + 1
print(freq2)

# OUTPUT:
# apple: 3
# banana: 2
# cherry: 1
# mango: 1


# ============================================================

# Q54: Combine two dicts — add values for common keys

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 4, "c": 1, "d": 5}
result = {}

# Get all unique keys from both dicts
all_keys = set(d1) | set(d2)

for key in all_keys:
    # .get(key, 0) returns 0 if key doesn't exist
    result[key] = d1.get(key, 0) + d2.get(key, 0)

print(f"Combined dict: {result}")

# OUTPUT: {'a':1, 'b':6, 'c':4, 'd':5}
# b: 2+4=6, c: 3+1=4, a: only in d1=1, d: only in d2=5


# ============================================================
# SECTION 11: EXCEPTION HANDLING QUESTIONS
# ============================================================

# Q55: Handle division by zero exception

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    else:
        print(f"Result: {result}")
        return result
    finally:
        print("Division operation attempted")

safe_divide(10, 2)   # works fine
safe_divide(10, 0)   # handles exception

# OUTPUT:
# Result: 5.0
# Division operation attempted
# Error: Cannot divide by zero!
# Division operation attempted


# ============================================================

# Q56: Handle ValueError when converting input to int

def get_integer():
    while True:
        try:
            n = int(input("Enter a valid integer: "))
            return n
        except ValueError:
            print("Invalid input! Please enter a number, not text.")

num = get_integer()
print(f"You entered: {num}")

# If user types "abc" → "Invalid input!" and asks again
# Loop continues until valid integer is entered


# ============================================================

# Q57: Handle multiple exceptions

def process_data(data, index):
    try:
        value = data[index]
        result = 100 / value
        print(f"Result: {result}")
    except IndexError:
        print(f"Error: Index {index} is out of range!")
    except ZeroDivisionError:
        print("Error: Value at that index is 0, can't divide!")
    except TypeError:
        print("Error: Value is not a number!")
    except Exception as e:
        print(f"Unexpected error: {e}")

my_list = [5, 0, "hello", 10]

process_data(my_list, 0)    # works: 100/5 = 20.0
process_data(my_list, 1)    # ZeroDivisionError
process_data(my_list, 2)    # TypeError
process_data(my_list, 10)   # IndexError

# OUTPUT:
# Result: 20.0
# Error: Value at that index is 0, can't divide!
# Error: Value is not a number!
# Error: Index 10 is out of range!


# ============================================================

# Q58: Use raise to validate age input

def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer!")
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age cannot be more than 150!")
    return age

# Test cases:
test_ages = [25, -5, 200, "twenty"]

for a in test_ages:
    try:
        result = set_age(a)
        print(f"Age set successfully: {result}")
    except (ValueError, TypeError) as e:
        print(f"Error for {a}: {e}")

# OUTPUT:
# Age set successfully: 25
# Error for -5: Age cannot be negative!
# Error for 200: Age cannot be more than 150!
# Error for twenty: Age must be an integer!


# ============================================================
# SECTION 12: FILE HANDLING QUESTIONS
# ============================================================

# Q59: Create a file, write to it, read it back

# WRITE to file
with open("test.txt", "w") as f:
    f.write("Hello World\n")
    f.write("Python is awesome\n")
    f.write("File handling is easy\n")

print("File written successfully!")

# READ entire file
with open("test.txt", "r") as f:
    content = f.read()
    print("\nFile contents:")
    print(content)

# READ line by line
with open("test.txt", "r") as f:
    print("Line by line:")
    for line in f:
        print(line.strip())   # strip() removes \n

# OUTPUT:
# File written successfully!
# File contents:
# Hello World
# Python is awesome
# File handling is easy


# ============================================================

# Q60: Append new content to existing file

with open("test.txt", "a") as f:
    f.write("New line added via append mode\n")
    f.write("Original content is preserved!\n")

# Verify by reading
with open("test.txt", "r") as f:
    print(f.read())

# "a" mode adds to END — does NOT overwrite existing content


# ============================================================

# Q61: Simple contact book using file handling

def add_contact(name, phone):
    with open("contacts.txt", "a") as f:
        f.write(f"{name},{phone}\n")
    print(f"Contact {name} added!")

def view_contacts():
    try:
        with open("contacts.txt", "r") as f:
            contacts = f.readlines()
            if not contacts:
                print("No contacts found!")
                return
            print("\n--- CONTACTS ---")
            for i, contact in enumerate(contacts, 1):
                name, phone = contact.strip().split(",")
                print(f"{i}. {name}: {phone}")
    except FileNotFoundError:
        print("No contacts file found. Add a contact first!")

# Test:
add_contact("Akarsh", "9876543210")
add_contact("Riya", "8765432109")
add_contact("Arjun", "7654321098")
view_contacts()

# OUTPUT:
# Contact Akarsh added!
# Contact Riya added!
# Contact Arjun added!
# --- CONTACTS ---
# 1. Akarsh: 9876543210
# 2. Riya: 8765432109
# 3. Arjun: 7654321098


# ============================================================
# SECTION 13: OOP QUESTIONS
# ============================================================

# Q62: Create a simple class with attributes and methods

class Dog:
    # Class attribute — shared by all dogs
    species = "Canis lupus familiaris"

    def __init__(self, name, age, breed):
        # Instance attributes — unique per dog
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}, Breed: {self.breed}")

# Creating objects
dog1 = Dog("Buddy", 3, "Labrador")
dog2 = Dog("Max", 5, "German Shepherd")

dog1.bark()
dog2.bark()
dog1.info()
print(f"Species: {Dog.species}")

# OUTPUT:
# Buddy says: Woof! Woof!
# Max says: Woof! Woof!
# Name: Buddy, Age: 3, Breed: Labrador
# Species: Canis lupus familiaris


# ============================================================

# Q63: Bank Account class — real world OOP example

class BankAccount:
    bank_name = "Python Bank"   # class attribute

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance    # private attribute

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self.__balance += amount
        print(f"✅ Deposited ₹{amount}. New balance: ₹{self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")
        if amount > self.__balance:
            print(f"❌ Insufficient funds! Available: ₹{self.__balance}")
        else:
            self.__balance -= amount
            print(f"✅ Withdrawn ₹{amount}. New balance: ₹{self.__balance}")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account[{self.owner}] Balance: ₹{self.__balance}"

# Testing:
acc = BankAccount("Akarsh", 1000)
print(acc)
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)    # insufficient funds
print(f"Final balance: ₹{acc.get_balance()}")

# OUTPUT:
# Account[Akarsh] Balance: ₹1000
# ✅ Deposited ₹500. New balance: ₹1500
# ✅ Withdrawn ₹200. New balance: ₹1300
# ❌ Insufficient funds! Available: ₹1300
# Final balance: ₹1300


# ============================================================

# Q64: Inheritance — Animal hierarchy

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)   # call parent constructor
        self.breed = breed

    def sound(self):    # overrides parent's sound()
        print(f"{self.name} says: Woof!")

    def fetch(self):
        print(f"{self.name} is fetching the ball!")

class Cat(Animal):
    def sound(self):    # overrides parent's sound()
        print(f"{self.name} says: Meow!")

    def purr(self):
        print(f"{self.name} is purring...")

class Bird(Animal):
    def sound(self):
        print(f"{self.name} says: Tweet!")

    def fly(self):
        print(f"{self.name} is flying!")

# Testing:
dog = Dog("Buddy", 3, "Labrador")
cat = Cat("Whiskers", 2)
bird = Bird("Tweety", 1)

dog.eat()         # inherited from Animal
dog.sound()       # overridden in Dog
dog.fetch()       # Dog's own method
cat.sound()       # overridden in Cat
bird.fly()        # Bird's own method

# Polymorphism:
print("\n--- All Animals Making Sounds ---")
animals = [Dog("Rex", 4, "Pug"), Cat("Luna", 3), Bird("Rio", 2)]
for animal in animals:
    animal.sound()    # same method name, different behavior

# OUTPUT:
# Buddy is eating
# Buddy says: Woof!
# Buddy is fetching the ball!
# Whiskers says: Meow!
# Tweety is flying!
# --- All Animals Making Sounds ---
# Rex says: Woof!
# Luna says: Meow!
# Rio says: Tweet!


# ============================================================

# Q65: Encapsulation — Student class with getters and setters

class Student:
    def __init__(self, name, age, marks):
        self.name = name              # public
        self._age = age               # protected
        self.__marks = marks          # private

    # Getter for private attribute
    def get_marks(self):
        return self.__marks

    # Setter with validation
    def set_marks(self, marks):
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100!")
        self.__marks = marks

    def get_grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 80:
            return "B"
        elif self.__marks >= 70:
            return "C"
        elif self.__marks >= 60:
            return "D"
        else:
            return "F"

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"Marks: {self.__marks}")
        print(f"Grade: {self.get_grade()}")

s = Student("Riya", 20, 85)
s.display()
s.set_marks(92)
print(f"\nUpdated marks: {s.get_marks()}")
print(f"Updated grade: {s.get_grade()}")

# Try to access private directly:
# print(s.__marks)  ← AttributeError
# But this works (name mangling):
# print(s._Student__marks)  ← 92

# OUTPUT:
# Name: Riya
# Age: 20
# Marks: 85
# Grade: B
# Updated marks: 92
# Updated grade: A


# ============================================================

# Q66: Abstract class — Shape hierarchy

from abc import ABC, abstractmethod
import math

class Shape(ABC):   # Abstract base class
    @abstractmethod
    def area(self):         # must be implemented by subclass
        pass

    @abstractmethod
    def perimeter(self):    # must be implemented by subclass
        pass

    def display(self):      # concrete method — inherited as is
        print(f"Shape: {self.__class__.__name__}")
        print(f"Area: {self.area():.2f}")
        print(f"Perimeter: {self.perimeter():.2f}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))

    def perimeter(self):
        return self.a + self.b + self.c

# shape = Shape()  ← TypeError! Can't instantiate abstract class

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]
for shape in shapes:
    shape.display()
    print()

# OUTPUT:
# Shape: Circle
# Area: 78.54
# Perimeter: 31.42
#
# Shape: Rectangle
# Area: 24.00
# Perimeter: 20.00
#
# Shape: Triangle
# Area: 6.00
# Perimeter: 12.00


# ============================================================
# SECTION 14: ADVANCED QUESTIONS
# ============================================================

# Q67: Lambda + map + filter

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map: square every number
squared = list(map(lambda x: x**2, numbers))
print(f"Squared: {squared}")

# filter: keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Evens: {evens}")

# map + filter combined: square only even numbers
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(f"Even squares: {result}")

# OUTPUT:
# Squared: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Evens: [2, 4, 6, 8, 10]
# Even squares: [4, 16, 36, 64, 100]


# ============================================================

# Q68: List, Dict, Set comprehensions

# List comprehension: squares of 1-10
squares = [x**2 for x in range(1, 11)]
print(f"Squares: {squares}")

# With condition: only even squares
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# With if-else: label each number
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 6)]
print(f"Labels: {labels}")

# Dict comprehension: word and its length
words = ["python", "java", "javascript", "c"]
word_lengths = {word: len(word) for word in words}
print(f"Word lengths: {word_lengths}")

# Set comprehension: unique remainders when dividing by 3
remainders = {x % 3 for x in range(20)}
print(f"Remainders mod 3: {remainders}")

# Nested list comprehension: multiplication table as list
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
for row in table:
    print(row)

# OUTPUT:
# Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Even squares: [4, 16, 36, 64, 100]
# Labels: ['Odd', 'Even', 'Odd', 'Even', 'Odd']
# Word lengths: {'python': 6, 'java': 4, 'javascript': 10, 'c': 1}
# Remainders mod 3: {0, 1, 2}


# ============================================================

# Q69: Decorator — timer decorator (real-world use)

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

@timer
def fast_function():
    return sum(range(1000000))

result1 = slow_function()
result2 = fast_function()

print(f"Slow result: {result1}")
print(f"Fast result: {result2}")

# OUTPUT (approximate):
# slow_function took 0.0800 seconds
# fast_function took 0.0200 seconds
# (fast is faster because sum() is implemented in C)


# ============================================================

# Q70: FINAL PROJECT — Student Report Card System
# Uses: classes, OOP, file handling, exception handling, loops

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.subjects = {}

    def add_marks(self, subject, marks):
        if not 0 <= marks <= 100:
            raise ValueError(f"Marks must be 0-100, got {marks}")
        self.subjects[subject] = marks

    def get_total(self):
        return sum(self.subjects.values())

    def get_percentage(self):
        if not self.subjects:
            return 0
        return (self.get_total() / (len(self.subjects) * 100)) * 100

    def get_grade(self):
        pct = self.get_percentage()
        if pct >= 90: return "A+"
        elif pct >= 80: return "A"
        elif pct >= 70: return "B"
        elif pct >= 60: return "C"
        elif pct >= 50: return "D"
        else: return "F"

    def display_report(self):
        print("=" * 40)
        print(f"   STUDENT REPORT CARD")
        print("=" * 40)
        print(f"Name    : {self.name}")
        print(f"Roll No : {self.roll_no}")
        print("-" * 40)
        print(f"{'Subject':<20} {'Marks':>10}")
        print("-" * 40)
        for subject, marks in self.subjects.items():
            print(f"{subject:<20} {marks:>10}")
        print("-" * 40)
        print(f"{'Total':<20} {self.get_total():>10}")
        print(f"{'Percentage':<20} {self.get_percentage():>9.1f}%")
        print(f"{'Grade':<20} {self.get_grade():>10}")
        print("=" * 40)

    def save_to_file(self):
        filename = f"{self.roll_no}_report.txt"
        with open(filename, "w") as f:
            f.write(f"Student Report Card\n")
            f.write(f"Name: {self.name}\n")
            f.write(f"Roll No: {self.roll_no}\n")
            for subject, marks in self.subjects.items():
                f.write(f"{subject}: {marks}\n")
            f.write(f"Total: {self.get_total()}\n")
            f.write(f"Percentage: {self.get_percentage():.1f}%\n")
            f.write(f"Grade: {self.get_grade()}\n")
        print(f"Report saved to {filename}")

# Testing the complete system:
try:
    s1 = Student("Akarsh Vyas", "CS001")
    s1.add_marks("Python", 95)
    s1.add_marks("Mathematics", 88)
    s1.add_marks("Physics", 79)
    s1.add_marks("Chemistry", 83)
    s1.add_marks("English", 91)
    s1.display_report()
    s1.save_to_file()

except ValueError as e:
    print(f"Error: {e}")

# OUTPUT:
# ========================================
#    STUDENT REPORT CARD
# ========================================
# Name    : Akarsh Vyas
# Roll No : CS001
# ----------------------------------------
# Subject                  Marks
# ----------------------------------------
# Python                      95
# Mathematics                 88
# Physics                     79
# Chemistry                   83
# English                     91
# ----------------------------------------
# Total                      436
# Percentage                87.2%
# Grade                        A
# ========================================
# Report saved to CS001_report.txt


# ============================================================
# PHASE 1 COMPLETE — ALL QUESTIONS SOLVED
# ============================================================

# TOPICS COVERED IN SOLUTIONS:
# ✅ Variables and Data Types
# ✅ String indexing and slicing
# ✅ Type conversion
# ✅ Operators and expressions
# ✅ All conditional questions (even/odd, voter, leap year, temp)
# ✅ All for loop questions (table, factorial, prime, palindrome)
# ✅ All while loop questions (digit separation, reverse, game)
# ✅ Functions (default args, *args, **kwargs, return)
# ✅ List operations and questions
# ✅ Dictionary questions
# ✅ Exception handling
# ✅ File handling + contact book project
# ✅ OOP (class, object, inheritance, polymorphism)
# ✅ Encapsulation (private, protected, public)
# ✅ Abstraction (ABC, shapes hierarchy)
# ✅ Advanced (lambda, map, filter, comprehensions, decorators)
# ✅ Final Project (Student Report Card)

# 🔜 NEXT PHASE: NumPy
# Arrays, vectorization, broadcasting
# Foundation of all data science in Python