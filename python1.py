# ============================================================
# ORIGIN OF PYTHON & ITS EXECUTION PROCESS
# Deep Dive — Interview + Concept Ready
# ============================================================


# ============================================================
# PART 1: ORIGIN OF PYTHON
# ============================================================

# WHO CREATED PYTHON?
# Creator : Guido van Rossum
# Nickname: "Benevolent Dictator For Life" (BDFL) of Python
# He led Python development for decades before stepping down in 2018

# WHEN WAS PYTHON CREATED?
# Late 1980s → Guido started working on Python
# December 1989 → Guido began writing the implementation
# February 1991 → Python 0.9.0 publicly released (first ever version)
# 1994 → Python 1.0 released (major first stable version)
# 2000 → Python 2.0 released (garbage collection, list comprehensions)
# 2008 → Python 3.0 released (major redesign, broke backward compatibility)
# Today → Python 3.x is the standard (Python 2 officially dead Jan 2020)

# WHY THE NAME "PYTHON"?
# NOT named after the snake!
# Guido was a fan of "Monty Python's Flying Circus"
# A British comedy TV show from the 1970s
# He wanted the language to be fun and easy — matching the show's spirit
# The snake logo came later (designed by O'Reilly media)
# Now the snake is the universal symbol of Python

# WHERE WAS IT CREATED?
# Guido was working at Centrum Wiskunde & Informatica (CWI)
# A national research institute in Amsterdam, Netherlands
# He created Python during Christmas holidays 1989
# He wanted a hobby project for the holiday break
# That holiday project became one of the world's most used languages

# WHAT PROBLEM WAS PYTHON SOLVING?
# Before Python, Guido worked on a language called ABC
# ABC was great for beginners but had limitations:
# - Couldn't easily extend with C code
# - No access to system calls (OS level)
# - Not suitable for professional scripting
# Python was designed to fix all these problems
# Goal: simple syntax + powerful capabilities + extensible

# PYTHON'S DESIGN PHILOSOPHY:
# Guido wrote the "Zen of Python" — 19 guiding principles
# Access it anytime by typing: import this
# Key principles:
# "Beautiful is better than ugly"
# "Simple is better than complex"
# "Readability counts"
# "There should be one obvious way to do it"
# This philosophy is WHY Python looks so clean compared to C++ or Java

# PYTHON VERSION HISTORY (important for interviews):
# Python 1.0 (1994) → basic features, lambda, map, filter
# Python 2.0 (2000) → list comprehensions, garbage collector, unicode
# Python 2.7 (2010) → last of Python 2 series
# Python 3.0 (2008) → major overhaul, print() as function, better unicode
# Python 3.6 (2016) → f-strings introduced (we use this!)
# Python 3.8 (2019) → walrus operator :=
# Python 3.10 (2021) → match-case (structural pattern matching)
# Python 3.12+ (2023+) → current versions, performance improvements
# Python 2 END OF LIFE → January 1, 2020 (no more updates/support)

# WHY PYTHON BECAME SO POPULAR:
# 1. Readable syntax → looks almost like English
# 2. Versatile → web, data science, ML, automation, scripting
# 3. Huge community → millions of developers, tons of libraries
# 4. Free and open source → anyone can use and contribute
# 5. Cross-platform → runs on Windows, Mac, Linux without changes
# 6. Massive library ecosystem → NumPy, Pandas, TensorFlow, Django etc.
# 7. Great for beginners AND professionals

# REAL WORLD ANALOGY FOR PYTHON'S BIRTH:
# Think of ABC language as a good recipe book
# but it only works in one specific kitchen
# Guido created Python as a recipe book that works in ANY kitchen
# Can be extended with any ingredient (C libraries)
# Can interact with the kitchen equipment (OS system calls)
# And reads like plain English so anyone can follow it


# ============================================================
# PART 2: HOW PYTHON EXECUTES YOUR CODE
# ============================================================

# FIRST — TWO TYPES OF LANGUAGES:

# TYPE 1: COMPILED LANGUAGES (C, C++, Java partially)
# Source code → COMPILER translates ENTIRE code at once → machine code
# Machine code runs directly on CPU
# FAST execution (code already in CPU language)
# But: must compile before running, platform-specific executable

# TYPE 2: INTERPRETED LANGUAGES (Python, JavaScript, Ruby)
# Source code → INTERPRETER translates line by line → executes immediately
# No separate compilation step needed
# SLOWER execution (translating while running)
# But: easier to debug, platform independent, faster development

# PYTHON IS INTERPRETED — but the full story is more interesting
# Python actually has a TWO STEP execution process internally
# Most people only know step 2 — knowing step 1 impresses interviewers


# ============================================================
# PYTHON EXECUTION PROCESS — STEP BY STEP
# ============================================================

# STEP 1: SOURCE CODE → BYTECODE (Compilation Phase)
# When you run a .py file, Python FIRST compiles it to bytecode
# Bytecode = intermediate low-level code (NOT machine code)
# Bytecode is stored in .pyc files inside __pycache__ folder
# This step happens AUTOMATICALLY — you never see it happening
# Bytecode is platform independent (runs on any OS)

# Example:
# You write:  hello.py
# Python creates: __pycache__/hello.cpython-311.pyc
# The .pyc file contains bytecode (binary format, not human readable)

# WHY BYTECODE AND NOT DIRECT MACHINE CODE?
# Machine code is specific to CPU architecture (x86, ARM, etc.)
# Bytecode is NEUTRAL — works on any machine that has PVM
# This is Python's "write once, run anywhere" principle

# STEP 2: BYTECODE → EXECUTION (PVM Phase)
# PVM = Python Virtual Machine
# PVM is installed when you install Python
# PVM reads bytecode instruction by instruction and EXECUTES each one
# PVM translates bytecode to actual machine code at runtime

# COMPLETE FLOW DIAGRAM:
# hello.py (source code you write)
#     ↓
# [Python Compiler]  ← automatic, hidden from you
#     ↓
# hello.pyc (bytecode in __pycache__)
#     ↓
# [PVM - Python Virtual Machine]
#     ↓
# Execution (output on screen)

# REAL WORLD ANALOGY:
# Imagine you write a letter in English (source code)
# A translator converts it to a special simplified language (bytecode)
# A machine reads that simplified language and acts on it (PVM)
# The final action = output you see


# ============================================================
# CPython — THE MAIN PYTHON IMPLEMENTATION
# ============================================================

# When most people say "Python" they mean CPython
# CPython = Python interpreter written in C language
# It is the REFERENCE implementation — the official standard Python
# Downloaded from python.org = CPython

# OTHER PYTHON IMPLEMENTATIONS (important for interviews):

# PyPy:
# Python interpreter written in Python itself (and RPython)
# Uses JIT (Just In Time) compilation
# JIT = compiles frequently used code to machine code while running
# Result: PyPy is 5x to 10x FASTER than CPython for many programs
# Used when speed matters (games, heavy computations)

# Jython:
# Python implementation written in Java
# Runs on JVM (Java Virtual Machine)
# Can use Java libraries directly in Python code
# Used when you need to integrate Python with Java systems

# IronPython:
# Python implementation for .NET framework (Microsoft)
# Runs on CLR (Common Language Runtime)
# Can use .NET/C# libraries in Python
# Used in Microsoft ecosystem

# MicroPython:
# Stripped-down Python for microcontrollers
# Runs on tiny devices like Arduino, Raspberry Pi Pico
# Very limited memory (as little as 256KB RAM)
# Used in IoT (Internet of Things) devices

# Brython:
# Python that runs in web browsers
# Translates Python to JavaScript
# Lets you write Python for front-end web development

# SUMMARY TABLE:
# Implementation | Written In | Runs On          | Special Use
# CPython        | C          | OS directly      | Standard Python (most used)
# PyPy           | Python/C   | OS (with JIT)    | Speed-critical programs
# Jython         | Java       | JVM              | Java integration
# IronPython     | C#         | .NET/CLR         | Microsoft/.NET ecosystem
# MicroPython    | C          | Microcontrollers | IoT devices
# Brython        | JavaScript | Web Browser      | Front-end Python


# ============================================================
# THE PVM IN DETAIL
# ============================================================

# PVM = Python Virtual Machine
# It is a SOFTWARE machine — not physical hardware
# Acts as a layer between bytecode and actual hardware

# PVM RESPONSIBILITIES:
# 1. Read bytecode instructions one by one
# 2. Manage memory (allocation and garbage collection)
# 3. Handle exceptions during execution
# 4. Manage the call stack (tracks which function is running)
# 5. Interact with OS for file I/O, network etc.

# CALL STACK (important concept):
# Every time a function is called → PVM creates a "stack frame"
# Stack frame holds: local variables, parameters, return address
# When function returns → stack frame is destroyed
# Stack overflow = too many nested function calls (infinite recursion)

# GARBAGE COLLECTION:
# Python automatically manages memory (unlike C/C++)
# When an object has NO more references → garbage collector frees it
# Main mechanism: Reference Counting
# Each object tracks how many variables point to it
# When count reaches 0 → memory freed automatically
# Additional: Cyclic garbage collector for circular references

# REFERENCE COUNTING EXAMPLE:
# x = [1, 2, 3]   → list object reference count = 1
# y = x            → reference count = 2 (both x and y point to it)
# x = None         → reference count = 1 (only y points to it)
# y = None         → reference count = 0 → GARBAGE COLLECTED (memory freed)


# ============================================================
# GIL — GLOBAL INTERPRETER LOCK (Advanced Interview Topic)
# ============================================================

# GIL = Global Interpreter Lock
# A MUTEX (lock) in CPython that allows only ONE thread to execute
# Python bytecode at a time — even on multi-core processors

# WHY DOES GIL EXIST?
# Python's memory management (reference counting) is NOT thread-safe
# Without GIL: two threads could modify reference count simultaneously
# This would cause memory corruption and crashes
# GIL was added as a simple fix to make CPython thread-safe

# IMPACT OF GIL:
# For CPU-bound tasks (math, loops) → threading in Python is SLOW
# Because only one thread runs Python bytecode at a time
# For I/O-bound tasks (file read, network requests) → threads still help
# Because during I/O wait, GIL is released (other threads can run)

# HOW TO BYPASS GIL:
# Use multiprocessing module (separate processes, each has own GIL)
# Use C extensions (numpy, etc. release GIL during computation)
# Use PyPy (has different GIL behavior)
# Python 3.12+ is working on making GIL optional (experimental)

# REAL WORLD ANALOGY FOR GIL:
# Imagine a kitchen (Python interpreter) with one chef knife (GIL)
# Multiple cooks (threads) want to use it
# Only ONE cook can use the knife at a time
# Other cooks must wait
# Even if you have 8 burners (8 CPU cores), only 1 cook chops at a time


# ============================================================
# PYTHON VS OTHER LANGUAGES — EXECUTION COMPARISON
# ============================================================

# C/C++:
# Source → Compiled to machine code → runs directly on CPU
# Fastest execution
# Must recompile for each OS/architecture
# Manual memory management (malloc, free)

# Java:
# Source → Compiled to bytecode (JVM bytecode)
# JVM executes bytecode with JIT compilation
# "Write once run anywhere"
# Automatic garbage collection
# Similar to Python but statically typed

# Python:
# Source → Compiled to bytecode (PVM bytecode)
# PVM executes bytecode
# Slowest of the three (no JIT in CPython)
# Automatic garbage collection
# Dynamic typing → more flexibility but slower

# JavaScript:
# Source → Interpreted by browser's JS engine (V8, SpiderMonkey)
# V8 uses JIT → very fast for a scripting language
# Python is generally slower than modern JavaScript

# WHY PYTHON IS SLOWER BUT STILL PREFERRED FOR ML/AI:
# ML heavy lifting is done by NumPy, TensorFlow etc.
# These libraries are written in C/C++ internally
# Python is just the "control layer" — the actual math runs in C
# So you get Python's simplicity + C's speed


# ============================================================
# INTERVIEW QUESTIONS — ORIGIN & EXECUTION
# ============================================================

# Q1: Who created Python and when?
# A: Guido van Rossum, started 1989, first released February 1991

# Q2: Why is Python named Python?
# A: Named after "Monty Python's Flying Circus" TV show
#    NOT after the snake (logo came later)

# Q3: Is Python compiled or interpreted?
# A: Both! Python first compiles source to bytecode (.pyc)
#    Then PVM interprets bytecode line by line
#    Technically: compiled to bytecode, then interpreted

# Q4: What is bytecode in Python?
# A: Intermediate, platform-independent code
#    Generated from .py file, stored in .pyc inside __pycache__
#    Executed by PVM — not human readable, not machine code

# Q5: What is PVM?
# A: Python Virtual Machine — software that executes Python bytecode
#    Part of Python installation, manages memory and execution

# Q6: What is CPython?
# A: Official reference implementation of Python, written in C
#    What you download from python.org
#    Most widely used Python implementation

# Q7: What is PyPy and how is it different from CPython?
# A: PyPy is an alternative Python interpreter with JIT compilation
#    JIT = compiles hot code to machine code at runtime
#    PyPy is 5-10x faster than CPython for CPU-intensive tasks

# Q8: What is the GIL in Python?
# A: Global Interpreter Lock — allows only one thread to run
#    Python bytecode at a time in CPython
#    Ensures thread safety for memory management
#    Limitation for multi-threaded CPU-bound programs

# Q9: What is the difference between Python 2 and Python 3?
# A: Key differences:
#    print statement (Python 2) vs print() function (Python 3)
#    Integer division: 5/2=2 (Python 2) vs 5/2=2.5 (Python 3)
#    Unicode: strings are bytes in Python 2, unicode in Python 3
#    Python 2 EOL = January 1, 2020

# Q10: What is __pycache__?
# A: Folder automatically created by Python
#    Stores compiled bytecode (.pyc files)
#    Next time you run same file — Python uses cached bytecode
#    Skips recompilation if source hasn't changed → faster startup

# Q11: What is garbage collection in Python?
# A: Automatic memory management
#    Primary: Reference counting (frees when count = 0)
#    Secondary: Cyclic garbage collector (handles circular references)

# Q12: Why is Python slow compared to C++?
# A: Dynamic typing → type checking at runtime (C++ at compile time)
#    No JIT in CPython → bytecode interpreted, not compiled to machine code
#    GIL → prevents true multi-threading
#    High-level abstractions → more overhead per operation


# ============================================================
# QUICK REVISION SUMMARY
# ============================================================

# ORIGIN:
# Creator   → Guido van Rossum
# Year      → 1989 (development), 1991 (first release)
# Named after → Monty Python's Flying Circus (comedy show)
# Created at → CWI, Amsterdam, Netherlands
# Inspired by → ABC language (wanted to fix ABC's limitations)
# Philosophy → Simple, readable, beautiful code (Zen of Python)
# Current    → Python 3.x (Python 2 dead since Jan 2020)

# EXECUTION FLOW:
# Step 1: .py (source code)
# Step 2: Python Compiler → .pyc (bytecode) in __pycache__
# Step 3: PVM reads bytecode → executes → output

# KEY TERMS:
# CPython   → official Python (written in C) — from python.org
# PyPy      → fast Python with JIT compilation
# Bytecode  → intermediate code (not machine code, not source)
# PVM       → software that runs bytecode
# GIL       → lock that allows only one thread at a time in CPython
# __pycache__ → folder storing compiled .pyc bytecode files