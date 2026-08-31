
# NumPy Complete Notes

---

## 1. Introduction

- This video/topic covers **NumPy** — how arrays are created, how NumPy operations are performed, plus small hands-on projects/exercises.
- **Prerequisite:** Python basics (data structures, functions, modules, packages). Without Python fundamentals, NumPy will be hard to follow.
- **NumPy** = **Num**erical **Py**thon → a **library** of Python.
- Topics covered in this session:
  1. What are NumPy arrays & how they're created
  2. 1D vs 2D (and higher-dimensional) arrays
  3. Random number generation
  4. Array attributes & methods
  5. Reshaping & resizing
  6. Indexing & slicing (vectors and matrices)
  7. Boolean indexing
  8. Arithmetic operations & broadcasting
  9. Deep copy vs shallow copy
  10. Matrix operations (multiplication, transpose)
  11. Stacking and splitting arrays
  12. Practical exercises (Sudoku validity check, student marks analysis)

---

## 2. Notebooks — What & Why

- A **Notebook** is a special file used for interactive coding, with extension **`.ipynb`** (compare: a plain Python file has extension `.py`).
- A notebook lets you:
  - Write and run code, and see the output immediately (cell by cell)
  - Add notes/markdown text, equations, images, and charts — all in one place
- Notebooks are essential in **Data Science** because of a field called **Data Visualization**, where working purely in `.py` scripts becomes cumbersome for showing charts/graphs alongside code and explanation.

### Ways to Create/Use a Notebook

**A. Anaconda Distribution + Jupyter Notebook**
- **Anaconda** is a *distribution* — when installed, it pre-installs most common data science libraries (NumPy, Pandas, Matplotlib, Seaborn, Scikit-learn, etc.), so you don't need to manually `pip install` each one.
- Steps:
  1. Search "Anaconda" → go to the download page → provide email, verify, then reach the "Download Now" page.
  2. Download the installer for your OS (Windows/Mac) — it's a large file since it bundles many packages.
  3. Install it — during installation, check/tick all the recommended options (warnings are usually safe to ignore).
  4. After installing, open the **Anaconda Navigator** application.
  5. In Navigator, find **Jupyter Notebook** ("web-based interactive computing notebook environment") → click **Launch**.
  6. This opens a terminal (Jupyter's own terminal, not the system terminal) and then a browser tab (Jupyter is browser/web-based).
  7. To open your working folder:
     - Use `cd <path>` (Change Directory) to navigate to your folder (e.g., a folder on Desktop).
     - You can copy the folder path from Finder (Mac) — right-click → "Copy Path" — and paste it into the terminal after `cd`.
     - Once inside the folder, type `jupyter notebook` and press Enter — this reopens Jupyter directly inside that folder.
  8. Alternative shortcut: Right-click the folder → **Open Terminal** → type `jupyter notebook` directly (works on some systems, not all).
  9. If errors occur, try running Anaconda Navigator **"as Administrator."**
  10. Inside the Jupyter Notebook interface, click **New** → choose a Python (conda environment) kernel to create a new notebook.

**B. VS Code**
- Install the **Jupyter extension** in VS Code (Extensions → search "Jupyter").
- Open an existing `.ipynb` file, or create a new one.
- Before running any cell, you must **Select a Kernel** (a Python environment) — choose either:
  - Your Conda environment (has all Anaconda-installed libraries), or
  - The Global Python environment (may lack libraries like NumPy, Pandas, Matplotlib, Seaborn).
- **Problem:** If you use the Global environment (not Anaconda's), NumPy/Pandas/etc. are **not pre-installed**. You must install each library manually:
  ```
  pip install numpy
  ```
  - This is why professional developers often provide a **`requirements.txt`** file listing all needed packages, which users install before running the project.

**C. Google Colab**
- Cloud-based; **no installation needed** — everything (NumPy, Pandas, etc.) comes **pre-installed**.
- Syncs with your Google account/Drive — notebooks and files are saved to your Drive.
- Create a notebook: Go to Colab → "New Notebook".
- **Downside:** Runs on the cloud, so a slow internet connection can make execution slower.
- **Major advantage: Free GPU support** — very useful for training larger Machine Learning / Deep Learning models (e.g., RNNs, CNNs) later on.

### Recommended Jupyter Settings
- **Theme:** Settings → Themes → switch to **JupyterLab Dark** (easier on the eyes).
- **Settings → Editor:**
  - Enable **Auto Completion** (very helpful since NumPy/data science libraries have thousands of functions you won't memorize).
  - Enable **Auto Close Brackets**.

### Basic Notebook Usage
- A notebook is made of **cells**.
- Run/execute the current cell and move to the next: **Shift + Enter**.
- You can create multiple cells; each executes independently, but **all cells share the same session/state** — a variable or function defined in one cell can be used in another cell below (or even above, once run) since they are interconnected within the same kernel session.
- To add cells below in Jupyter: click on the side and press `B` (or use the `+`/toolbar).

---

## 3. Origin Story of NumPy (Brief History)

- Python was always powerful for math computations compared to other languages, but it originally lacked a proper **array** data structure (it only had lists, tuples, dictionaries, sets — no true array type).
- **1995** — Jim Hugunin created the **Numeric** library, which added array support to Python — but its performance wasn't great.
- **Early 2000s** — The **Space Telescope Science Institute** developed another library called **Numarray**, aiming to improve on Numeric's power — but it was **not compatible** with Numeric, causing fragmentation.
- **2005** — **Travis Oliphant** combined **Numeric** and **Numarray** into a single library and named it **NumPy**. This finally brought unified, powerful array support to Python.
- **Why is NumPy so fast?**
  - NumPy is written internally in **C**, which is a compiled and very fast language.
  - Python itself is an **interpreted language** and is comparatively slow.
  - By linking C code to Python (via the NumPy library), NumPy achieves major speed gains.
  - **NumPy can be up to ~50x faster than native Python lists** for numerical operations.

---

## 4. NumPy Arrays — Basics

### Setup
```python
import numpy as np
```
- NumPy is imported as `np` by convention, so you don't have to type `numpy` every time before calling its many functions.

### Python List vs NumPy Array

| Feature | Python List | NumPy Array |
|---|---|---|
| Data types allowed | **Heterogeneous** — can mix ints, floats, strings, lists, dicts, etc. in one list | **Homogeneous** — all elements must be of the **same data type** |
| Performance | Slow (interpreted) | Fast — up to ~50x faster (compiled C backend) |
| Memory efficiency | Low (more space used) | High (less space used, more efficient) |
| Vector/math operations | Manual loops required | Native support (vectorized operations), no explicit loops needed |

- **Type coercion rule:** If a NumPy array is created from a list containing mixed types, NumPy automatically **converts all elements to a single common data type**:
  - If any string is present → everything becomes a string (Unicode, shown as dtype `<U32` or similar).
  - If no strings, but a float is present → everything becomes a float.
  - (No integer-only list stays as strings unless a string is present.)

### Creating a Basic Array
```python
arr = np.array([1, 2, 3, 4])
print(arr)
# Output looks like: [1 2 3 4]   (no commas, unlike a printed Python list)
```
- The core function is `np.array()`, which takes a **list** (or list of lists) and converts it into a NumPy array.
- Difference in printed appearance: A list prints as `[1, 2, 3, 4]` (with commas); an array prints as `[1 2 3 4]` (space-separated, no commas).

### Vectors vs Matrices vs Tensors
- **Vector** = a **1-dimensional (1D)** array — a single row of values.
  ```python
  v = np.array([1, 2, 3, 4, 5])   # 1D → vector
  ```
- **Matrix** = a **2-dimensional (2D)** array — has rows and columns.
  ```python
  m = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])       # 2D → matrix
  ```
  - A plain Python list containing nested lists (e.g. `[[1,2,3],[4,5,6],[7,8,9]]`) does **not** behave as a true 2D structure when printed directly as a list — only converting it via `np.array()` gives it real 2D matrix behavior/shape.
- Beyond 2D (3D, 4D, and higher dimensions) are called **Tensors** (this is where the name "TensorFlow" comes from — a library for deep learning, to be covered later).

---

## 5. Array Generation Functions

### `np.arange()`
- Works like Python's `range()`, but generates a NumPy array. Syntax: `np.arange(start, stop, step)`.
- `stop` is **exclusive** (just like `range`).
```python
np.arange(1, 11)        # [1 2 3 4 5 6 7 8 9 10]
np.arange(1, 11, 2)     # [1 3 5 7 9]   (step of 2)
```
- Good practice: always save the generated array into a variable, e.g. `arr = np.arange(...)`.

### `np.zeros()`
```python
np.zeros(6)          # 1D array of six 0.0's
np.zeros((6, 6))      # 2D matrix: 6 rows x 6 columns, all zeros
np.zeros((4, 8))      # 4 rows, 8 columns
```
- **Rows** = horizontal groupings; **Columns** = vertical groupings.
- Shape is given as `(rows, columns)`.

### `np.ones()`
```python
np.ones(6)            # 1D array of six 1.0's
np.ones((6, 6))        # 6x6 matrix of ones
```

### `np.linspace()` — Linear Spacing
- `np.linspace(start, stop, num)` returns `num` **evenly (linearly) spaced** numbers over the interval `[start, stop]` — **both start and stop are included**.
- Use **Shift + Tab** inside Jupyter to view a function's docstring/signature quickly.
```python
np.linspace(1, 5, 2)    # [1. 5.]                     -> 2 evenly spaced points
np.linspace(1, 5, 3)    # [1. 3. 5.]                  -> spacing of 2 between each
np.linspace(1, 5, 5)    # [1. 2. 3. 4. 5.]             -> spacing of 1
np.linspace(1, 5, 10)   # 10 evenly spaced points between 1 and 5
np.linspace(0, 1, 100)  # 100 evenly spaced points between 0 and 1
```
- **Key difference from `arange`:** `arange` uses a fixed **step size** and the count of numbers varies; `linspace` uses a fixed **count of numbers** and calculates the step size to keep spacing even.

### Random Number Generation (`np.random`)
- NumPy's random module works closely with (and is inspired by) Python's built-in `random` library.

**`np.random.rand()`** — generates random floats **between 0 and 1** (uniform distribution). This relates to the statistical concept of **Normalization** (scaling values to a 0–1 range).
```python
np.random.rand(5)     # 5 random floats in [0, 1)
np.random.rand(10)    # 10 random floats in [0, 1) -> a vector (1 set of brackets)
```
- Note: A single pair of brackets `[ ]` = vector (1D); double brackets `[[ ]]` = matrix (2D).

**`np.random.randn()`** — generates random floats from a **standard normal distribution**, roughly centered around 0, typically ranging between about **-3 and +3**. This relates to the statistical concept of **Standardization**.
```python
np.random.randn(10)
```

**`np.random.randint(low, high, size)`** — generates random **integers**.
```python
np.random.randint(6)              # 1 random integer between 0 and 6
np.random.randint(10, 20, size=10) # 10 random integers between 10 and 20
```
- (Presenter mentioned they may cover full Statistics fundamentals in a future video if there's audience interest.)

---

## 6. Array Attributes vs Methods (Concept Recap)

- **Attribute** = a variable defined inside a class/object — accessed **without parentheses**.
- **Method** = a function defined inside a class/object — accessed **with parentheses** (called).

### Common Attributes
Given:
```python
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
```
| Attribute | Meaning | Example |
|---|---|---|
| `arr.shape` | (rows, columns) — no parentheses since it's an attribute | `(3, 3)` |
| `arr.size` | Total number of elements | `9` |
| `arr.dtype` | Data type of elements | `int64` (or similar) |

### Common Methods
| Method | Meaning |
|---|---|
| `arr.min()` | Minimum element in the array |
| `arr.max()` | Maximum element in the array |
| `arr.sum()` | Sum of **all** elements (flattened) |
| `np.sum(arr, axis=0)` | Column-wise sum (sums going **down** each column) |
| `np.sum(arr, axis=1)` | Row-wise sum (sums **across** each row) |
| `arr.mean()` | Average (mean) of all elements |
| `arr.std()` | Standard deviation of all elements |
| `arr.argmax()` | **Index** of the maximum element |
| `arr.argmin()` | **Index** of the minimum element |

### Understanding `axis`
- **`axis=0`** → operates **down the columns** (column-wise result — one result per column).
- **`axis=1`** → operates **across the rows** (row-wise result — one result per row).
- This is a very common point of confusion — always double-check which axis you need based on whether you want per-row or per-column results.

---

## 7. Reshaping and Resizing

### `.reshape(rows, cols)`
- Changes the *shape/view* of an existing array **without changing its data**, as long as the total element count matches: `rows × cols` must equal the original number of elements.
```python
arr = np.arange(1, 31)          # 30 elements (1 to 30)
arr2 = arr.reshape(6, 5)         # 6 rows x 5 columns = 30 elements — valid
# arr.reshape(5, 5)              # INVALID -> 5x5 = 25 ≠ 30 elements -> error
```

### `.resize(rows, cols)`
- Similar to reshape, but modifies the array **in place** (directly changes the original array's shape/storage), rather than just returning a new reshaped view.

---

## 8. Indexing and Slicing

### 8.1 Vectors (1D Arrays)

Setup:
```python
arr = np.arange(11, 21)   # [11 12 13 14 15 16 17 18 19 20]
```

**Indexing** — works exactly like Python lists, zero-based:
```python
arr[6]     # index 6 -> value 17
arr[9]     # index 9 -> value 20
```

**Slicing** — `arr[start:end:step]`
- `start` is inclusive, `end` is **exclusive** (must write one index past the last element you want).
- To slice `12, 13, 14, 15`: `arr[1:5]` (index 1 up to, but not including, index 5).
```python
arr[1:5]     # [12 13 14 15]
```
**Default slicing values:**
- Omitting `start` defaults it to `0`: `arr[:5]` → from beginning up to index 5.
- Omitting `end` defaults it to the array's end: `arr[3:]` → from index 3 to the end.
- Omitting both: `arr[:]` → the entire array.

**Using a step in slicing:**
```python
arr[3:9:2]   # start at index 3, step by 2, stop before index 9 -> [14 16 18 20]
```
- Syntax: `arr[start:end:step]` — the third value (after the second colon) is the **step size**.

**Saving a slice:**
```python
arr_slice = arr[1:5]
```
(Slices and array copies behave specially — see the **Deep vs Shallow Copy** section below.)

### 8.2 Matrices (2D Arrays)

Setup:
```python
arr = np.arange(1, 31).reshape(6, 5)   # 6 rows, 5 columns, values 1–30
```

**Single-index access on a 2D array targets a whole ROW:**
```python
arr[0]     # entire first row: [1 2 3 4 5]
arr[1]     # entire second row: [6 7 8 9 10]
arr[5]     # entire sixth (last) row: [26 27 28 29 30]
```

**Row & column indexing (targeting a single element):** `arr[row_index, col_index]`
- Row indexing goes first, then column indexing.
```python
arr[0, 0]    # row 0, col 0 -> 1
arr[0, 4]    # row 0, col 4 -> 5
arr[5, 3]    # row 5, col 3 -> 30
```

**Slicing a rectangular block of a matrix:** `arr[row_start:row_end, col_start:col_end]`
- Example: to extract elements `2, 3, 7, 8` (rows 0–1, columns 1–2):
```python
arr[0:2, 1:3]
```
- Example: to extract `19, 20, 24, 25, 29, 30` (rows 3 to end, columns 3 to end):
```python
arr[3:, 3:]
```

**Extracting an entire column:**
```python
arr[:, 1]   # all rows, column index 1 -> returns as a 1D vector, e.g. [3 8 13 18 23 28]
```
- Note: when you slice out a single column or row, the result is returned as a flattened 1D array/vector, even though it came from a 2D matrix.

### 8.3 Boolean Indexing
- You can create a **boolean mask** (array of `True`/`False`) by applying a condition to an array, then use that mask to filter elements.

```python
arr = np.arange(11, 21)          # [11 12 13 14 15 16 17 18 19 20]
bool_index = arr % 2 == 0        # [False True False True ... ] (True where even)
arr = arr[bool_index]            # keeps only elements where mask is True
print(arr)                       # [12 14 16 18 20]
```
- The boolean mask (`arr % 2 == 0`) must have the **same length** as the array it's applied to.
- Anywhere the mask is `True`, that element is **kept**; anywhere it's `False`, that element is **dropped**.
- **Important caveat:** After filtering, the array's length changes — running the same filter line again (on the already-filtered array) can cause a shape-mismatch error, since the mask was computed for the original (longer) array. Re-run from the top (recreate the original array) before reapplying.
- Boolean indexing overlaps conceptually with the **Operations** section below (modulo `%` operator is an arithmetic operation).

---

## 9. Arithmetic Operations on Arrays

### Basic Rule
- To perform element-wise arithmetic between two arrays, **both arrays must have the same shape/size** (same number of elements). Mismatched shapes raise an error:
  > `operands could not be broadcast together with shapes ...`

### Setup
```python
a1 = np.array([1, 2, 3, 4, 5])
a2 = np.array([6, 7, 8, 9, 10])
```

### Element-wise Operations
```python
a1 + a2    # [ 7  9 11 13 15]   -> element-wise addition
a1 - a2    # [-5 -5 -5 -5 -5]   -> element-wise subtraction
a1 * a2    # element-wise multiplication (NOT true matrix multiplication)
a1 / a2    # element-wise division
a1 // a2   # element-wise FLOOR division
a1 ** a2   # element-wise exponentiation (power) — e.g. 1**6, 2**7, 3**8...
```
- **Important:** `a1 * a2` on two 1D arrays of equal length performs simple **element-wise multiplication** (position-by-position), which is **NOT** the same as true matrix multiplication (dot product) — see Section 11 below.
- No explicit `for` loop is required — NumPy applies the operation across all elements automatically. (Contrast with Python lists, where you would need a manual loop or list comprehension.)

---

## 10. Broadcasting

- **Broadcasting** = NumPy's ability to apply an operation between a **single scalar value** (or a smaller-shaped array) and **every element** of a larger array, without writing an explicit loop.

### Example (Vector)
```python
arr = np.array([10, 20, 30, 40])
arr + 10      # [20 30 40 50]  -> 10 is "broadcast" and added to every element
```
- Without NumPy (using a plain Python list), you would need a `for` loop:
  ```python
  result = [x + 10 for x in my_list]   # manual approach for lists
  ```

### Example (Matrix)
```python
arr2 = np.arange(1, 26).reshape(5, 5)
arr2 + 10     # adds 10 to every element in the 2D matrix
arr2 * 2      # multiplies every element by 2
```
- Broadcasting works identically for both 1D vectors and 2D (or higher) matrices — it is **not restricted to vectors only**.

---

## 11. Deep Copy vs Shallow Copy

This is a critical concept for avoiding accidental data corruption.

### Case 1: Slicing an array → creates an **independent copy** (deep-copy-like behavior)
```python
a = np.arange(1, 21)
slice_ = a[0:5]        # slice out a portion
slice_ = slice_ * 10   # modify the slice
print(a)                # a is UNCHANGED — slicing created a separate memory location
```
- When you **slice** a portion out of an array, NumPy allocates that slice at a **different memory location**. Changes to the slice do **not** affect the original array.
> ⚠️ **Note for accuracy:** In real NumPy, basic slicing (`a[0:5]`) actually returns a **view** (shares memory with the original) by default — modifying a slice normally *does* affect the original array. However, in the video's demonstrated example, reassigning the sliced variable with `slice_ = slice_ * 10` created a **new array object** (because `*` creates a new array rather than modifying in place), which is why the original stayed unchanged in that specific case. If you want to guarantee independence from the original when slicing, explicitly use `.copy()` (see Case 3), or use in-place operations carefully.

### Case 2: Direct assignment (`b = a`) → shares the SAME memory reference (true shallow behavior)
```python
a = np.array([1, 2, 3, ...])
b = a                    # b now points to the SAME array in memory as a
b[0] = 99
print(a)                  # a[0] is ALSO 99 — changing b changed a!
```
- When you do `b = a`, you are **not** creating a new array — `b` is just another name/reference pointing to the **same location** in memory (RAM) as `a`. Modifying `b` modifies `a` too.

### Case 3: Explicit copy using `.copy()` → creates a true independent copy
```python
b = a.copy()
b[0] = 99
print(a)     # a is UNCHANGED — b.copy() made a fully independent array
print(b)     # only b is changed
```
- Use `.copy()` whenever you want to be **certain** that modifying one array will **not** affect the other.

---

## 12. Matrix Operations

### 12.1 Matrix Multiplication (True Dot Product)
- Regular `*` between two 2D arrays does simple element-wise (position-based) multiplication — **not** proper matrix multiplication.
- **True matrix multiplication (dot product)** rule: each element of the result = (sum of) row-of-first-matrix elements multiplied pairwise with column-of-second-matrix elements.
  - Example: For matrices `A = [[1,2],[3,4]]` and `B = [[5,6],[7,8]]`:
    - Result[0][0] = `1*5 + 2*7` = `19`
    - Result[0][1] = `1*6 + 2*8` = `22`
    - (and so on for remaining rows/columns)

**Two ways to perform true matrix multiplication:**
```python
A @ B              # @ operator performs matrix (dot product) multiplication
np.dot(A, B)        # equivalent alternative using np.dot()
```

### 12.2 Transpose
- **Transpose** flips a matrix so that **rows become columns** and **columns become rows**.
```python
A.T     # transpose of A
```
- Example: If `A = [[1,2],[3,4]]`, then `A.T = [[1,3],[2,4]]`.

---

## 13. Advanced Array Manipulation

### 13.1 Stacking Arrays
- Stacking joins two (or more) arrays together. **Important:** stacking works properly on **vectors (1D arrays)**, not directly on already-2D matrices in the examples shown.

Setup:
```python
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
```

**Vertical Stack — `np.vstack()`**
- Stacks arrays **row-wise** (one array becomes a new row below the other).
```python
np.vstack((a, b))
# [[1 2 3 4]
#  [5 6 7 8]]
```
- Note: takes a **tuple** `(a, b)` as a single positional argument.

**Horizontal Stack — `np.hstack()`**
- Stacks arrays **side by side** (end-to-end into one longer row).
```python
np.hstack((a, b))
# [1 2 3 4 5 6 7 8]
```

**Column Stack — `np.column_stack()`**
- Converts each input 1D array into a **column** of a 2D result (useful when you want a true 2D structure rather than one long flattened row).
```python
np.column_stack((a, b))
# [[1 5]
#  [2 6]
#  [3 7]
#  [4 8]]
```

### 13.2 Splitting Arrays
Setup:
```python
c = np.arange(1, 17).reshape(4, 4)   # 4x4 matrix, values 1–16
```

**Horizontal Split — `np.hsplit(array, n)`**
- Splits the array into `n` equal parts **horizontally** (splits along columns — cutting the array into left/right pieces).
```python
np.hsplit(c, 2)   # splits into 2 equal parts
```
- The number of parts **must divide evenly** into the number of columns, otherwise you get an error:
  > `array split does not result in an equal division`

**Vertical Split — `np.vsplit(array, n)`**
- Splits the array into `n` equal parts **vertically** (splits along rows — cutting the array into top/bottom pieces).
```python
np.vsplit(c, 2)   # splits into 2 equal parts (top half, bottom half)
np.vsplit(c, 4)   # splits into 4 equal parts, one per original row
```
- Result is a **list of arrays** — you can iterate over them:
```python
parts = np.vsplit(c, 4)
for part in parts:
    print(part)     # each part is still a 2D array (not flattened to 1D)
```

---

## 14. Practical Exercises

### Exercise 1: Validate a Sudoku Grid

**Sudoku rules used for validation:**
- A 9×9 grid is divided into **9 sub-blocks of 3×3** each.
- There are **9 rows** and **9 columns**.
- **Validity condition:** Every row, every column, and every 3×3 block must contain each number from 1–9 exactly once. Therefore, the **sum of every row = 45**, the **sum of every column = 45**, and the **sum of every 3×3 block = 45** (since 1+2+...+9 = 45).

**Step 1 — Setup**
```python
import numpy as np
s = np.array([...])   # a 9x9 sudoku grid
```

**Step 2 — Check row sums**
```python
row_sums = np.sum(s, axis=1)   # axis=1 -> sum across each row
for i in row_sums:
    if i != 45:
        print("Sudoku is NOT valid")
        break
else:
    print("For rows, it is valid")
```
- **Axis reminder:** `axis=1` gives per-row sums; `axis=0` gives per-column sums.

**Step 3 — Check column sums**
```python
col_sums = np.sum(s, axis=0)   # axis=0 -> sum down each column
# same validity check as above, comparing each to 45
```

**Step 4 — Check each 3×3 block sum**
- Use nested loops with a step of 3 to iterate over block boundaries:
```python
for i in range(0, 9, 3):        # i = 0, 3, 6 -> row block starts
    for j in range(0, 9, 3):    # j = 0, 3, 6 -> column block starts
        block = s[i:i+3, j:j+3]
        print(block)
        print(np.sum(block))    # should equal 45 for every block
```
- This confirms there are **9 total 3×3 blocks**, and each must sum to 45 for the Sudoku to be considered valid.

### Exercise 2: Student Marks Analysis (2D Array)

**Setup — a 5×3 NumPy array:**
- Rows = 5 students (Student 1 to Student 5)
- Columns = `[Age, Math Marks, Science Marks]`
```python
data = np.array([
    [18, 85, 95],
    [19, 92, 88],
    [17, 76, 81],
    [18, 65, 70],
    [20, 90, 85]
])   # example structure — actual values from the video vary
```

**Q1. Get the shape of the matrix**
```python
data.shape    # e.g. (5, 3) -> 5 rows, 3 columns
```

**Q2. Find the average age of students**
```python
np.mean(data[:, 0])   # select all rows, column 0 (age), then take mean
```

**Q3. Extract Math marks of all students**
```python
data[:, 1]    # all rows, column index 1 (math marks)
```

**Q4. Find the highest Science marks**
```python
np.max(data[:, 2])   # all rows, column index 2 (science marks)
```

**Q5. Get details of the student(s) who scored more than 90 in Math**
```python
data[data[:, 1] > 90]
```
- Pattern: build a boolean condition on a specific column, then pass that condition **back into `data[...]`** to filter and return the **full matching row(s)**.

**Q6. Increase Math marks of all students by 5**
```python
data[:, 1] = data[:, 1] + 5     # or: data[:, 1] += 5
```
- ⚠️ **Common mistake to watch for:** Writing `data = data[:, 1] + 5` (instead of `data[:, 1] = ...`) will **overwrite the entire `data` variable** with just the modified column, destroying the rest of the matrix. Always assign back into the **same sliced portion**, not to the whole `data` variable. If this happens, re-run all cells from the top to restore original data before retrying.

**Q7. Find how many students are younger than 19**
```python
young_mask = data[:, 0] < 19
young_students = data[young_mask]
print(len(young_students))   # count of students younger than 19
```

**Q8. Calculate the average marks in each subject (column-wise mean)**
```python
np.mean(data[:, 1:], axis=0)
```
- `data[:, 1:]` selects both Math and Science columns; `axis=0` gives one average **per column** (Math average, Science average).

**Q9. Get data of students who scored at least 80 in BOTH subjects**
```python
data[(data[:, 1] >= 80) & (data[:, 2] >= 80)]
```
- Use the `&` operator (NumPy's element-wise AND) to combine two boolean conditions, with each condition wrapped in parentheses.
- (Note: this differs from plain Python's `and` keyword — NumPy requires `&`/`|` with parentheses for element-wise boolean array combination; this will be explained further when covering Pandas.)

**Q10. Replace all Science marks less than 75 with 0**
```python
data[:, 2][data[:, 2] < 75] = 0
```
- Pattern: select the target column (`data[:, 2]`), then apply a boolean condition **on that same column slice**, then assign the replacement value (`0`) only to the matching (filtered) elements — not to the entire column.

---

## 15. Additional Important NumPy Concepts (Supplementary — Not Covered in the Video, but Commonly Needed)

These are gaps worth knowing to have a complete, practical picture of NumPy:

### 15.1 Data Types (`dtype`)
- You can explicitly set a data type when creating an array:
  ```python
  np.array([1, 2, 3], dtype=float)
  np.array([1, 2, 3], dtype=np.int32)
  ```
- Convert an existing array's type: `arr.astype(np.float64)`.

### 15.2 Identity / Diagonal Matrices
```python
np.eye(4)          # 4x4 Identity matrix (1's on diagonal, 0's elsewhere)
np.identity(3)      # same as above, 3x3
np.diag([1,2,3])    # creates a diagonal matrix from a 1D array
```

### 15.3 `np.full()` and `np.empty()`
```python
np.full((3,3), 7)    # 3x3 array filled entirely with the value 7
np.empty((2,2))       # uninitialized array (fast but contains garbage values — use with caution)
```

### 15.4 Useful Aggregate/Utility Functions
```python
np.sort(arr)            # returns a sorted copy of the array
np.unique(arr)           # returns sorted unique elements
np.median(arr)            # median value
np.var(arr)                # variance
np.cumsum(arr)             # cumulative sum
np.concatenate((a, b))     # joins arrays along an existing axis (general-purpose alternative to vstack/hstack)
np.where(condition, x, y)  # element-wise conditional selection (like an if-else across the array)
np.clip(arr, min, max)     # limits values to a given range
```

### 15.5 `np.where()` — Conditional Logic (very commonly used, similar spirit to Exercise Q10 above)
```python
np.where(arr > 5, arr, 0)   # keep value if > 5, otherwise replace with 0
```
- This is often a cleaner alternative to boolean-mask assignment for conditional replacement.

### 15.6 Flattening Arrays
```python
arr.flatten()    # returns a 1D copy of a multi-dimensional array
arr.ravel()        # similar, but returns a view when possible (more memory-efficient)
```

### 15.7 Concatenation vs Stacking
- `np.concatenate()` is the general-purpose joining function; `vstack`/`hstack`/`column_stack` are convenience wrappers around it for common cases.

### 15.8 Broadcasting Rules (Formal)
NumPy broadcasting follows specific compatibility rules when array shapes differ (not just scalar + array):
1. Compare shapes from the **rightmost** dimension.
2. Two dimensions are compatible if they are **equal**, or if **one of them is 1**.
3. Arrays with fewer dimensions are padded with size-1 dimensions on the left.
- Example: a `(3,3)` array and a `(3,)` array (or `(1,3)`) can broadcast together; a `(3,3)` and `(4,)` cannot.

### 15.9 Views vs Copies (More Precise Note)
- **Basic slicing** (`arr[1:5]`) typically returns a **view** (shares memory with original) — changing the view *can* change the original, and vice versa.
- **Fancy indexing** (using a list/array of indices, or boolean masks, e.g., `arr[[1,3,5]]` or `arr[mask]`) always returns a **copy**, not a view.
- Use `.copy()` explicitly whenever you need guaranteed independence, regardless of which indexing method you used — this removes ambiguity.

### 15.10 Vectorization — Why NumPy is Fast (Conceptual Summary)
- **Vectorization** means applying operations to entire arrays at once (in optimized, compiled C loops) instead of using explicit Python-level `for` loops.
- This is the core reason broadcasting and NumPy's arithmetic operators are so much faster than equivalent list-based Python loops.

### 15.11 NaN and Missing Value Handling (relevant for future Pandas work)
```python
np.nan                 # represents a missing/undefined numeric value
np.isnan(arr)            # boolean mask of where values are NaN
np.nanmean(arr)          # mean, ignoring NaN values
```

### 15.12 Random Seed (Reproducibility)
```python
np.random.seed(42)   # ensures random numbers generated afterward are reproducible across runs
```
- Important for reproducible experiments/testing when using `np.random` functions.

### 15.13 Array Dimensions Attribute
```python
arr.ndim    # number of dimensions (1 for vector, 2 for matrix, etc.)
```

---

## 16. Key Takeaways / Summary

- NumPy arrays are **homogeneous**, **memory-efficient**, and much **faster** than Python lists due to their C-based implementation and support for **vectorized operations**.
- **1D = vector, 2D = matrix, 3D+ = tensor.**
- Master **indexing/slicing** for both vectors and matrices — remember `array[row, column]` ordering for 2D.
- **Boolean indexing** (`arr[condition]`) is a powerful, loop-free way to filter and modify data.
- **Broadcasting** lets you apply scalar operations across entire arrays without explicit loops.
- Be careful about **views vs copies** — direct assignment (`b = a`) shares memory; use `.copy()` when independence is required.
- Use `@` or `np.dot()` for **true matrix multiplication**, not `*` (which is element-wise).
- `np.vstack`, `np.hstack`, `np.column_stack` for combining arrays; `np.hsplit`, `np.vsplit` for splitting them.
- These NumPy fundamentals are the foundation for later topics: **Pandas (DataFrames)**, **Machine Learning algorithms**, and **Deep Learning (TensorFlow, tensors)** — all rely heavily on NumPy arrays under the hood.

---

*Next topic in the series: Pandas.*
