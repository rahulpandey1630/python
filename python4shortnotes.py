# ============================================================
# PHASE 1 PYTHON — QUICK REVISION NOTES
# Short | Fast | Interview Ready
# ============================================================


# ============================================================
# 1. ORIGIN & EXECUTION
# ============================================================

# Creator  → Guido van Rossum | Year → 1989 dev, 1991 release
# Named after → Monty Python's Flying Circus (NOT the snake)
# Created at → CWI, Amsterdam, Netherlands

# EXECUTION FLOW:
# .py → [Compiler] → .pyc (bytecode) → [PVM] → Output
# Bytecode stored in → __pycache__ folder
# PVM = Python Virtual Machine (installed with Python)

# KEY TERMS:
# CPython  → official Python (written in C) — from python.org
# PyPy     → faster Python with JIT compilation (5-10x faster)
# GIL      → only ONE thread runs bytecode at a time (CPython)
# Bytecode → intermediate code (not machine code, not source)

# Python 2 → dead since Jan 1, 2020
# Python 3 → current standard (f-strings from 3.6)


# ============================================================
# 2. VARIABLES & NAMING
# ============================================================

# Variable = named container to store data in memory
name = "Akarsh"   # str
age  = 21         # int
gpa  = 9.2        # float
flag = True       # bool

# RULES (break = SyntaxError):
# ❌ 2name  → can't start with number
# ❌ my name → no spaces
# ❌ my-name → no special chars except _
# ❌ for = 5 → no reserved keywords

# CONVENTIONS:
# snake_case  → variables & functions  ✅ Python standard
# PascalCase  → Class names
# ALL_CAPS    → Constants (PI = 3.14)

# Dynamic typing → Python assigns type automatically
x = 10       # int
x = "hello"  # now str — Python allows this


# ============================================================
# 3. DATA TYPES
# ============================================================

# NUMBERS:
# int     → whole numbers         → age = 21
# float   → decimal numbers       → gpa = 9.2
# complex → real + imaginary      → c = 3 + 4j

# STRING:
# Any keyboard character in quotes
# Double or single quotes — both same
# Stores each char with Unicode value
# ord("A") → 65 | chr(65) → "A"

# BOOLEAN:
# Only True or False
# True = 1, False = 0 internally

# 7 FALSY VALUES (memorize!):
# 0, 0.0, False, "", [], {}, ()
# Everything else → Truthy


# ============================================================
# 4. STRINGS
# ============================================================

s = "Hello"
#    01234   positive index
#   -5-4-3-2-1  negative index

# INDEXING:
# s[0]  → H  |  s[-1] → o  |  s[1] → e

# SLICING: s[start : stop : step]
# stop is EXCLUSIVE (does not include)
# s[1:4]   → "ell"    (1,2,3 only)
# s[::2]   → "Hlo"    (every 2nd)
# s[::-1]  → "olleH"  (reverse)

# TYPE CONVERSION:
# int()   → "10"→10, 9.9→9 (truncates NOT rounds)
# float() → "3.14"→3.14
# str()   → 21→"21"
# bool()  → non-zero/non-empty→True, else False

# input() ALWAYS returns string — must convert manually!
# Implicit → Python auto converts (int+float = float)
# Explicit → you manually convert using int(), str() etc.

# COMMON TRAP:
# 0.1 + 0.2 = 0.30000000000000004 (float precision issue)


# ============================================================
# 5. OPERATORS
# ============================================================

# ARITHMETIC (7):
# +  -  *  /  //  %  **
# /  → ALWAYS returns float (10/2 = 2.0)
# // → floor division (10//3 = 3)
# %  → remainder (10%3 = 1)
# ** → power (2**3 = 8)

# ASSIGNMENT:
# =  +=  -=  *=  /=  //=  %=  **=
# x += 5 → same as x = x + 5

# COMPARISON (always returns bool):
# ==  !=  >  <  >=  <=
# = is assignment, == is comparison

# LOGICAL:
# and → True only if BOTH True
# or  → True if AT LEAST ONE True
# not → reverses boolean
# Short circuit: and skips 2nd if 1st False
#                or  skips 2nd if 1st True

# TRIVIAL ANSWERS:
# 126 > 130              → False
# (456==456) != (235==236) → True
# 12<10 or 45==56 or 15!=13 → True
# True and bool(0)       → False


# ============================================================
# 6. CONDITIONAL STATEMENTS
# ============================================================

# if → runs if True
# if-else → one block for True, one for False
# if-elif-else → multiple conditions, first match wins
# Python checks TOP TO BOTTOM, stops at first True

# SYNTAX:
# if condition:
#     code
# elif condition:
#     code
# else:
#     code

# INDENTATION = mandatory (4 spaces)
# Python uses spaces NOT {} like other languages

# LEAP YEAR FORMULA:
# (year%4==0 and year%100!=0) or (year%400==0)


# ============================================================
# 7. LOOPS
# ============================================================

# FOR → when you KNOW number of iterations
# WHILE → when you DON'T know, but know stop condition

# range(start, stop, step)
# stop is EXCLUSIVE
# range(1,6) → 1,2,3,4,5 (not 6)
# range(5,0,-1) → 5,4,3,2,1

# FOR LOOP:
# for i in range(n):  → 0 to n-1
# for char in string: → direct access to chars
# for i in range(len(s)): → access by index

# WHILE LOOP:
# while condition:
#     code
#     update_condition  ← MUST or infinite loop!

# BREAK    → exit loop immediately
# CONTINUE → skip current iteration, go to next
# ELSE     → runs ONLY if loop completed WITHOUT break

# KEY PATTERNS:
# Last digit    → n % 10
# Remove digit  → n // 10
# Reverse string → s[::-1]
# Even check    → n % 2 == 0
# Prime check   → loop from 2 to sqrt(n)+1


# ============================================================
# 8. FUNCTIONS
# ============================================================

# def function_name(parameters):
#     code
#     return value

# Parameters → variables in definition (placeholders)
# Arguments  → actual values passed when calling

# 3 TYPES OF ARGUMENTS:
# 1. Positional → matched by position add(3,5)
# 2. Keyword   → matched by name add(b=5, a=3)
# 3. Default   → has default value def greet(name="Guest")

# Default params MUST come AFTER non-default!
# def func(x, y=5): ✅  |  def func(x=5, y): ❌

# return → sends value back to caller
# No return → function returns None

# *args   → unlimited positional → stored as TUPLE
# **kwargs → unlimited keyword  → stored as DICT

# Lambda → anonymous one-line function
# square = lambda x: x**2
# check = lambda x: "Even" if x%2==0 else "Odd"


# ============================================================
# 9. DATA STRUCTURES — QUICK COMPARISON
# ============================================================

#           | Ordered | Mutable | Duplicates | Syntax
# List      |   Yes   |   Yes   |    Yes     |  []
# Tuple     |   Yes   |   No    |    Yes     |  ()
# Set       |   No    |   Yes   |    No      |  {}
# Dict      |   Yes   |   Yes   | Keys: No   |  {k:v}


# ============================================================
# 10. LIST
# ============================================================

# Mutable, Ordered, Duplicates, Heterogeneous
nums = [5, 2, 9, 1, 5, 6]

# METHODS (must know all):
# .append(x)     → add to END
# .insert(i,x)   → insert at index i
# .extend([x,y]) → add multiple to end
# .remove(x)     → remove first occurrence by VALUE
# .pop(i)        → remove by INDEX, returns removed item
# .index(x)      → find index of x
# .count(x)      → count occurrences
# .sort()        → sort ascending (in-place)
# .reverse()     → reverse (in-place)
# .copy()        → shallow copy
# .clear()       → remove all

# append vs extend:
# [1,2].append([3,4]) → [1,2,[3,4]]  (nested)
# [1,2].extend([3,4]) → [1,2,3,4]    (flat)

# remove vs pop:
# remove(val) → by value, returns nothing
# pop(idx)    → by index, returns removed item

# sort() vs sorted():
# nums.sort()   → modifies ORIGINAL
# sorted(nums)  → returns NEW list, original unchanged


# ============================================================
# 11. TUPLE
# ============================================================

# Immutable, Ordered, Duplicates, Heterogeneous
t = (5, 2, 9, 1)

# Only 2 methods:
# .index(x) → find index
# .count(x) → count occurrences

# Single element tuple MUST have comma:
# (5)  → just integer 5
# (5,) → tuple with one element ✅

# Tuple uses:
# Return multiple values from function
# Dictionary keys (lists can't be keys — unhashable)
# Data that should NOT change

# Unpacking:
x, y, z = (10, 20, 30)


# ============================================================
# 12. SET
# ============================================================

# Mutable, Unordered, NO duplicates, Semi-heterogeneous
s = {1, 2, 3}
s2 = set()   # empty set — {} is empty DICT not set!

# METHODS:
# .add(x)      → add element
# .remove(x)   → remove, ERROR if not found
# .discard(x)  → remove, NO error if not found
# .pop()       → remove RANDOM element
# .clear()     → remove all

# SET OPERATIONS:
# A.union(B)               → A | B  → all elements
# A.intersection(B)        → A & B  → common only
# A.difference(B)          → A - B  → in A not in B
# A.symmetric_difference(B)→ A ^ B  → in either not both

# Cannot store lists/dicts (unhashable/mutable)
# Use case: remove duplicates → list(set(nums))


# ============================================================
# 13. DICTIONARY
# ============================================================

# Mutable, Ordered(3.7+), Unique keys, Heterogeneous
d = {"name": "Akarsh", "age": 21}

# ACCESS:
# d["name"]       → "Akarsh" (KeyError if missing)
# d.get("name")   → "Akarsh" (None if missing — SAFE)
# d.get("x", 0)   → 0 if "x" missing (custom default)

# CRUD:
# d["city"] = "Mumbai"  → add new key
# d["age"]  = 22        → update existing
# del d["city"]         → delete key
# d.pop("age")          → delete + return value

# TRAVERSAL:
# for key in d:             → keys only
# for k,v in d.items():     → key + value
# for v in d.values():      → values only

# MERGE DICTS:
# {**d1, **d2}     → merge
# d1 | d2          → merge (Python 3.9+)
# d1.update(d2)    → d1 gets d2's items

# Keys = immutable (string, int, tuple)
# Lists as keys → TypeError (unhashable)


# ============================================================
# 14. EXCEPTION HANDLING
# ============================================================

# Errors (can't handle) → SyntaxError, IndentationError
# Exceptions (can handle) → runtime errors

# KEYWORDS:
# try     → risky code here
# except  → handle exception
# else    → runs if NO exception
# finally → runs ALWAYS (cleanup)
# raise   → manually throw exception

# SYNTAX:
# try:
#     risky code
# except SpecificError:
#     handle it
# except Exception as e:
#     print(e)  → catch all others
# else:
#     runs if no exception
# finally:
#     always runs

# COMMON EXCEPTIONS:
# ValueError       → wrong value (int("abc"))
# TypeError        → wrong type ("hi" + 5)
# ZeroDivisionError→ divide by zero
# IndexError       → index out of range
# KeyError         → key not in dict
# FileNotFoundError→ file doesn't exist
# NameError        → variable not defined

# raise example:
# if age < 0: raise ValueError("Age can't be negative")


# ============================================================
# 15. FILE HANDLING
# ============================================================

# MODES:
# "r" → Read (default, file must exist)
# "w" → Write (overwrites, creates if not exists)
# "a" → Append (adds to end, creates if not exists)
# "x" → Create (fails if already exists)

# ALWAYS use 'with' → auto closes file:
# with open("file.txt", "r") as f:
#     content = f.read()

# READ METHODS:
# f.read()       → entire file as string
# f.readline()   → one line
# f.readlines()  → all lines as list

# WRITE:
# f.write("text")  → write string

# "w" vs "a":
# w → OVERWRITES entire file ❌ existing data gone
# a → APPENDS to end ✅ existing data safe


# ============================================================
# 16. OOP — 4 PILLARS
# ============================================================

# CLASS = blueprint | OBJECT = instance (actual thing)

# class MyClass:
#     class_attr = value          # shared by all objects
#     def __init__(self, x):
#         self.x = x              # unique per object
#     def method(self):
#         return self.x

# self → refers to current object
# __init__ → constructor, auto-runs when object created

# ATTRIBUTE TYPES:
# Class attribute    → defined outside methods, shared
# Instance attribute → defined with self, unique per object

# METHOD TYPES:
# Instance method  → def method(self):
# Class method     → @classmethod + def method(cls):
# Static method    → @staticmethod + def method():


# ============================================================
# 17. INHERITANCE
# ============================================================

# class Child(Parent):  → Child gets all of Parent

# super() → call parent's method/constructor
# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)  → runs Parent's __init__
#         self.age = age

# TYPES:
# Single     → 1 parent, 1 child
# Multiple   → 2+ parents, 1 child → class C(A, B)
# Multilevel → grandparent→parent→child

# MRO (Method Resolution Order):
# Multiple inheritance → left to right order
# class C(A, B) → C checks A first, then B


# ============================================================
# 18. POLYMORPHISM
# ============================================================

# Same method name → different behavior per class

# Method Overriding → child redefines parent's method
# class Dog(Animal):
#     def sound(self):   → overrides Animal's sound()
#         print("Woof")

# Duck Typing → Python cares about METHOD not TYPE
# If object has the method → Python will call it
# "If it quacks like a duck → it's a duck"

# Method Overloading → NOT supported in Python
# Second definition REPLACES first


# ============================================================
# 19. ENCAPSULATION
# ============================================================

# Bundling data + methods + hiding internal details

# ACCESS MODIFIERS:
# Public    → self.name     → accessible everywhere
# Protected → self._name    → convention: don't access outside
# Private   → self.__name  → name mangling applied

# Name mangling:
# self.__salary → becomes → self._ClassName__salary
# Direct access → AttributeError


# ============================================================
# 20. ABSTRACTION
# ============================================================

# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self): pass   → subclass MUST implement

# Can't instantiate abstract class → TypeError
# Forces subclasses to follow a "contract"


# ============================================================
# 21. DUNDER METHODS
# ============================================================

# Special methods with __ prefix and suffix
# Auto-called for certain operations

# __init__  → object creation
# __str__   → print(object)
# __add__   → object + object
# __len__   → len(object)
# __eq__    → object == object


# ============================================================
# 22. ADVANCED CONCEPTS
# ============================================================

# DECORATOR:
# Function that modifies another function
# @decorator → same as func = decorator(func)
# def my_dec(func):
#     def wrapper():
#         # before
#         func()
#         # after
#     return wrapper

# COMPREHENSIONS:
# List: [x**2 for x in range(10) if x%2==0]
# Dict: {x: x**2 for x in range(5)}
# Set:  {x**2 for x in range(5)}

# MAP & FILTER:
# map(func, iterable)    → apply func to every item
# filter(func, iterable) → keep items where func returns True
# list(map(lambda x: x*2, [1,2,3]))   → [2,4,6]
# list(filter(lambda x: x>2, [1,2,3]))→ [3]

# MODULES:
# import math           → math.sqrt(16)
# from math import sqrt → sqrt(16)
# import math as m      → m.sqrt(16)
# Module = single .py file
# Package = folder of modules


# ============================================================
# INTERVIEW QUICK FIRE — MOST ASKED
# ============================================================

# Q: Interpreted or compiled?
# A: Both — compiled to bytecode, then PVM interprets

# Q: = vs ==?
# A: = assignment  |  == comparison

# Q: List vs Tuple?
# A: List mutable []  |  Tuple immutable ()

# Q: remove() vs discard() in set?
# A: remove → error if not found  |  discard → no error

# Q: dict[] vs dict.get()?
# A: [] → KeyError if missing  |  .get() → None if missing

# Q: break vs continue?
# A: break → exits loop  |  continue → skips current iteration

# Q: append vs extend?
# A: append([1,2]) → adds as single nested item
#    extend([1,2]) → adds each item individually (flat)

# Q: What does input() return?
# A: Always string — must convert with int(), float() etc.

# Q: 7 falsy values?
# A: 0, 0.0, False, "", [], {}, ()

# Q: What is self?
# A: Reference to current object/instance

# Q: What is __init__?
# A: Constructor — auto-runs when object is created

# Q: super()?
# A: Calls parent class method from child class

# Q: What is GIL?
# A: Allows only 1 thread to run Python bytecode at a time

# Q: How to reverse a string?
# A: s[::-1]

# Q: How to check if number is prime?
# A: Loop from 2 to int(n**0.5)+1, check if any divides n

# Q: Why use 'with' for files?
# A: Auto-closes file even if exception occurs

# Q: What is name mangling?
# A: __attr becomes _ClassName__attr (private simulation)

# Q: Difference between sort() and sorted()?
# A: sort() → modifies original  |  sorted() → returns new list


