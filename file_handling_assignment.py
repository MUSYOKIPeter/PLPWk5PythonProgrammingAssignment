# Task 1: File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("Good evening Mr. MUSYOKI Peter. Trust you are well. [1]\n") #This is Line 1 
        file.write("Come on, let's explore the 1947 - 1957 A LIFE OF ALETRNATIVES philosophy. [2]\n") #This is Line 2 
        file.write("47 & 57 - Non sine pericule (i.e., Not without danger): These are the answers to life, the universe, and everything. [3]\n") #This is Line 3 
    print("File 'my_file.txt' created successfully.")
except IOError:
    print("An error occurred while creating the file.") 


# Task 2: File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Contents of 'my_file.txt':")
        print(file.read())
except FileNotFoundError:
    print("The file 'my_file.txt' does not exist.")
except PermissionError:
    print("Permission denied to read the file.")


# Task 3: File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Adding another greeting, Good morning!\n")
        file.write("WAMBUI, Dorcas\n")
        file.write("2015 - 2025 UN DECADE OF ECOSYSTEM RESTORATION\n")
    print("Three lines appended to 'my_file.txt'.")
except IOError:
    print("An error occurred while appending to the file.")


# Task 4: Error Handling
try:
    with open("nonexistent_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file 'nonexistent_file.txt' does not exist.")
except PermissionError:
    print("Permission denied to read the file.")
finally:
    print("Program execution completed.")
