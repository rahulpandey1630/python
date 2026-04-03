
# ============================================================
# FILE MANAGER PROJECT
# Concepts: File Handling, Exception Handling, Pathlib, OS
# ============================================================

from pathlib import Path
import os


# ============================================================
# HELPER FUNCTION — shows all files and folders
# called inside every main function so user knows what exists
# ============================================================

def readfielandfolder():
    # Path('') = current working directory (where this .py file is)
    path = Path('')

    # rglob('*') = recursively find EVERYTHING
    # (all files + folders + subfolders)
    # list() converts the generator to a proper list
    items = list(path.rglob('*'))

    print("\n📁 ALL FILES AND FOLDERS:")
    print("-" * 35)

    # enumerate(items) gives (index, item) pairs
    # i starts at 0, so i+1 makes it start at 1 (looks cleaner)
    for i, item in enumerate(items):
        print(f"  {i+1} : {item}")

    print("-" * 35)


# ============================================================
# FUNCTION 1 — CREATE A FILE
# ============================================================

def createfile():
    try:
        # show existing files first so user doesn't duplicate names
        readfielandfolder()

        # ask user for the new file name
        name = input("\nPlease tell your file name :- ")

        # Path(name) creates a Path object
        # Path object lets us check existence, type etc easily
        p = Path(name)

        # p.exists() → True if file/folder already exists
        # we only create if it does NOT exist
        if not p.exists():

            # open(p, "w") → write mode
            # creates file if not exists
            # overwrites if exists (but we already checked above)
            with open(p, "w") as fs:
                data = input("What you want to write in this file :- ")
                # fs.write(data) → writes the string into file
                fs.write(data)

            print("✅ FILE CREATED SUCCESSFULLY")

        else:
            # file already exists → tell user
            print("⚠️  This file already exists!")

    except Exception as err:
        # catches ANY unexpected error and shows the message
        print(f"❌ An error occurred: {err}")


# ============================================================
# FUNCTION 2 — READ A FILE
# ============================================================

def readfile():
    try:
        # show all files so user can pick the right name
        readfielandfolder()

        name = input("\nWhich file do you want to read? :- ")

        p = Path(name)

        # p.exists() → file/folder must exist
        # p.is_file() → must be a FILE not a folder
        # both conditions needed to safely read
        if p.exists() and p.is_file():

            # open(p, 'r') → read mode (default mode)
            # file must exist for read mode (already checked above)
            with open(p, 'r') as fs:
                # fs.read() → reads ENTIRE file content as one string
                data = fs.read()
                print("\n📄 FILE CONTENT:")
                print("-" * 35)
                print(data)
                print("-" * 35)

            print("✅ Read successfully!")

        else:
            # file doesn't exist or path is a folder
            print("❌ The file does not exist!")

    except Exception as err:
        print(f"❌ An error occurred: {err}")


# ============================================================
# FUNCTION 3 — UPDATE A FILE
# 3 options: rename | overwrite content | append content
# ============================================================

def updatefile():
    try:
        # show existing files so user picks correct name
        readfielandfolder()

        name = input("\nTell which file you want to update :- ")

        p = Path(name)

        # only proceed if it's an existing file
        if p.exists() and p.is_file():

            # show update options to user
            print("\nUPDATE OPTIONS:")
            print("  press 1 → Rename the file")
            print("  press 2 → Overwrite (replace all content)")
            print("  press 3 → Append (add to existing content)")

            res = int(input("Tell your response :- "))

            # ----- OPTION 1: RENAME -----
            if res == 1:
                name2 = input("Tell your new file name :- ")
                p2 = Path(name2)
                # p.rename(p2) → renames file from p to p2
                p.rename(p2)
                print(f"✅ File renamed to '{name2}' successfully!")

            # ----- OPTION 2: OVERWRITE -----
            if res == 2:
                # open with 'w' mode → DELETES old content, writes new
                with open(p, 'w') as fs:
                    data = input("Tell what you want to write (this will overwrite) :- ")
                    fs.write(data)
                print("✅ File overwritten successfully!")

            # ----- OPTION 3: APPEND -----
            if res == 3:
                # open with 'a' mode → KEEPS old content, adds at END
                with open(p, 'a') as fs:
                    data = input("Tell what you want to append :- ")
                    # " " + data adds a space before new content
                    fs.write(" " + data)
                print("✅ Content appended successfully!")

        else:
            print("❌ File does not exist!")

    except ValueError:
        # if user types text instead of 1/2/3
        print("❌ Please enter a valid number (1, 2 or 3)!")

    except Exception as err:
        # NOTE: original code had missing f before string — bug!
        # print("an error occured as {err}") ← WRONG (no f-string)
        # corrected below:
        print(f"❌ An error occurred: {err}")


# ============================================================
# FUNCTION 4 — DELETE A FILE
# ============================================================

def deletefile():
    try:
        # show all files so user knows what to delete
        readfielandfolder()

        name = input("\nWhich file do you want to delete? :- ")

        p = Path(name)

        # only delete if file exists AND is actually a file
        # (safety check — prevents deleting folders accidentally)
        if p.exists() and p.is_file():

            # os.remove(name) → permanently deletes the file
            # alternative: p.unlink() does the same thing
            os.remove(name)

            print("✅ File deleted successfully!")

        else:
            # file not found → inform user
            print("❌ No such file exists!")

    except PermissionError:
        # file might be open in another program
        print("❌ Permission denied! File may be in use.")

    except Exception as err:
        print(f"❌ An error occurred: {err}")


# ============================================================
# MAIN PROGRAM — Menu driven interface
# ============================================================

# show menu options to user
print("=" * 35)
print("      📁 FILE MANAGER")
print("=" * 35)
print("  press 1 → Create a file")
print("  press 2 → Read a file")
print("  press 3 → Update a file")
print("  press 4 → Delete a file")
print("=" * 35)

# int(input()) → converts string input to integer for comparison
# if user types "abc" here → ValueError (not handled here — keep simple)
check = int(input("Please tell your response :- "))

# using if (not elif) so only exact match runs
# could also use elif — both work here since only one will match
if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()


# ============================================================
# CONCEPT SUMMARY — what each line/tool does
# ============================================================

# Path('')            → represents current directory
# Path('file.txt')    → represents a file path
# path.exists()       → True if file/folder exists on disk
# path.is_file()      → True if path points to a FILE
# path.is_dir()       → True if path points to a FOLDER
# path.rglob('*')     → finds ALL files+folders recursively
# path.rename(new)    → renames/moves the file
# path.stat().st_size → file size in bytes

# open(p, 'w')        → write mode  (creates/overwrites)
# open(p, 'r')        → read mode   (file must exist)
# open(p, 'a')        → append mode (adds to end)
# open(p, 'x')        → create mode (fails if exists)

# fs.write(data)      → writes string to file
# fs.read()           → reads entire file as string
# fs.readline()       → reads one line
# fs.readlines()      → reads all lines into a list

# os.remove(name)     → permanently deletes a file
# p.unlink()          → same as os.remove using pathlib

# with open() as fs:  → auto closes file after block ends
#                        even if exception occurs (safer!)

# enumerate(items)    → gives (index, value) pairs
#                        for i, item in enumerate(list)

