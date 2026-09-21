# File: homework1.py


# ---variables and Data Types---

a = 10
print(a)
print(type(a))
# integer, whole number
b = 1.5
print(b)
print(type(b))
# float, decimal number
c = 3j
print(c)
print(type(c))
# complex, number with real and imaginary parts
d = "Hello"
print(d)
print(type(d))
# string, sequence of characters
e = [1, 2, 3]
print(e)
print(type(e))
# list, ordered collection of items
f = {"name": "Ellan", "Favorite fruit": "strawberry"}
print(f)
print(type(f))
# dictionary, unordered collection of key-value pairs
g = (1, 2)
print(g)
print(type(g))
# tuple, ordered collection of items
h = ["apple", "banana", "strawberry"]
print(h)
print(type(h))
# set, unordered collection of unique items
i = True
print(i)
print(type(i))
# boolean, True or False
j = None
print(j)
print(type(j))
# NoneType, represents the absence of a value
k = [True, "Blue", 12]
print(k)
print(type(k))
# mixed data type, list can contain different data types
l = str(14)
print(l)
print(type(l))
# type conversion, converting an integer to a string
m = 1e4
print(m)
print(type(m))
# scientific notation, represents 1 * 10^4
# 1: 13. 2: int, float, complex, str, list, dict, tuple, set, bool, NoneType, mixed data type, type conversion, scientific notation
# 3: Well I mean, a lot of them have integers in them but none of them are the data type integer so I would say that none of the variables are the same data type.
# 4: The data type of l was type conversion. It's not an integer becuase it was converted to a string. str() converts whatevers inside to a string.
# 5: Range
n = range(5)
print(n)
print(type(n))
# Range, represents a sequence of numbers

# Booleans

print(10 > 9) # True, because 10 is greater than 9
print(10 == 9) # False, because 10 is not equal to 9
print(10 <= 9) # False, because 10 is not less than or equal to 9
print(bool("abc")) # True, because the string is not empty
print(bool(123)) # True, because the number is not zero
print(bool(["apple", "banana", "cherry"])) # True, because the list is not empty
print(bool(True)) # True, because the boolean value is True
print(bool(False)) # False, because the boolean value is False
print(bool(0)) # False, because the number is zero
print(bool("")) # False, because the string is empty
print(bool(" ")) # True, because the string is not empty
print(bool(())) # False, because the tuple is empty
print(bool([])) # False, because the list is empty
print(bool({})) # False, because the dictionary is empty
print(bool(True and False)) # False, because both sides have to be true
print(bool(True and True)) # True, because both sides are true
print(bool(False and False)) # False, because everythings is false
print(bool(True or False)) # True, because only one side has to be true when using or
print(bool(True or True)) # True, both sides are true
print(bool(False or False)) #False, both sides are false
print(bool(not False)) # True, because not False is True
print(bool(not True)) # False, because not True is False
# 1: If the inside makes sense or can only be true/one thing, it's probably true.
# 2: Maybe true and false because it's equally true and false.
print(bool(25>4)) # True, because 25 is greater than 4
print(bool(25<4)) # False, because 25 is not less than 4

# Operators

#arithmetic Operators
print(10 + 5) # 15, Addition
print(10 - 5) # 5, Subtraction
print(2*4) # 8, Multiplication
print(6/3) # 2.0, Division
print(5%2) # 1, Modulus, returns the remainder of the division
print(3**2) # 9, Exponentiation, 3 raised to the power of 2
print(15//2) # Floor division, returns the largest integer less than or equal to the division

# Comparison Operators
print(5 == 2) # False, compares if two numbers are equal
print(10 != 10) # False, compares if two numbers are not equal
print(2<5) # True,  less than
print(12>5) # True, greater than
print(5<=6) # True, less than or equal to
print(1>=10) # False, greater than or equal to

#assignment Operators
x = 5
x += 5
print(x) # 10, adds 5 to x and assigns the result to x
x -= 4
print(x) # 6, subtracts 4 from x and assigns the result to x
x *= 3
print(x) # 18, multiplies x by 3 and assigns the result to x

# Logical Operators

# and means both conditions have to be true for the statement to be true, if one is false then the whole thing is false (Ex: True and True = True, True and False = False)
# or means that only one condition has to be true for the statement to be true (Ex: True or False = True, False or False = False)
# not reverses the result (Ex: not True = False, not False = True)

# More Questions

# the difference between / and // is that / returns a float while // returns an integer
#the difference between % and // is that % returns the remainder of the division while // returns the largest integer less than or equal to the division
# I would use % to calculate the remainder. Ex 25 % 4 = 1
# Assignment operators assign a value to a variable after a calculation

# Strings

my_string = "hello"
print(my_string) # prints : hello
print(my_string[0]) # prints : h, first character of the string
print(my_string[1]) # prints : e, second character of the string
print(my_string[2]) # prints : l, third character of the string
print(my_string[3]) # prints : l, fourth character of the string
print(my_string[4]) # prints : o, fifth character of the string
print(my_string[-1]) # prints : o, last character of the string
print(my_string[1:3]) # prints : el, characters from index 1 to 2
print(my_string[0:5:2]) # prints : hlo, starting from 0 to 4, every second character
print(len(my_string)) # prints : 5, the length of the string
print(my_string + "goodbye") # prints : hellogoodbye, just literally adds both strings together
print(7 * my_string) # prints : hellohellohellohellohellohellohello, repeats the string 7 times

# Slicing is a way to get part of a string by specifying the start, end, and step size. I sliced my string in the print(my_string[0:5:2]) manipulation

name = "Oski"
print("Hello, my name is", name)
print(f"Hello, my name is {name}") # prints : Hello, my name in Oski, concatenates the string with the variable
# nothings different between the print statements, the second one is just a more effiecient way to do it since f strings are easier to read and write.

#Terminal commands

# Cd: Changes directories, use it to move to one folder to another. Ex: cd python
# Ls: listes the files and directories in the current directory. Ex: ls personal
# ls -a: lists all files and directories, including hidden ones. Ex: ls -a super_personal
# mkdir: creates a new directory. Ex: mkdir new_folder
# cat: displays the contents of a file. Ex: cat homework1.py
# pwd: prints the current working directory. Ex: pwd python
# cd ..: moves up one directory level. Ex: cd .. homework1
# cd .: stays in the current directory. Ex: cd . homework1
# cd ~: moves to the home directory. Ex: cd ~ desktop
# cp: copies a file or directory. Ex: cp homework1.py homework1_copy.py
# mv: moves a file or directory. Ex: mv homework1.py homework1
# rm: removes a file or directory. Ex: rm homework1.py
# clear: clears the terminal screen. Ex: clear
# grep: searches for a specific pattern in a file. Ex: grep "Hello" homework1.py

# 1:
# Touch: creates a new empty file. Ex: touch new_file.txt
# rmdir: removes an empty directory. Ex: rmdir old_folder
# echo: displays a message or writes text to a file. Ex: echo "Hello, World!" > hello.txt
# 2: the difference between ls and ls -a is that ls shows only the visible files and ls -a shows that plus the hidden files
# 3: A hidden file is a file that's not automatically visible in the directory listing
# 4:
# cp -a: preserves file attributes and copies directories recursively. Ex: cp -a homework1.py 
# cp -i: prompts for confirmation before overwriting an existing file. Ex: cp -i homework1.py 
# pwd -P: prints the physical path by resolving all symbolic links: Ex: pwd -P