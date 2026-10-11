#2.1

# git is the place where you can talk to your computer, github is where you can upload your code for other people
# the terminal is where (the application) you can type commands to your computer, the command line is where you atually type
# local repository is where your code is stored on your computer, remote repository is where your code is stored on github
# version control is a system that records changes to a file so you can look a back and see who changed what
# the staging area is where you put files that you want to commit then push to git hub
# git add is the command that puts files in the staging area
# git commit is the command that saves the changes you made to the local repository
# git push is the command that sends the changes you made to the local repository to the remote repository
# git pull is the command that gets the changes from the remote repository and puts them in your local repository
# pwd prints the current working directory
# ls lists the files in the current working directory
# cd changes the current working directory
# nano is a text editor that you can use to edit files in the terminal
# touch is a command that creates a new file
# mv is a command that moves or renames a file
# rm is a command that removes a file
# cat is a command that displays the contents of a file


# 2.2

# pwd
# ls
# cd .., cd brianna_repo, git pull origin main
# mv homework.py python_decal, mv homework.py judy_decal
# cd .., cd judy_decal
# cat homework.py
# git add homework.py, git commit -m "added homework.py", git push origin main
# Judy didn't add her work first before pushing, to resovle this do the command git add homeowrk.py


# 3

# 3.1 

def checkDataType(data):
    return type(data)

print(checkDataType(True))
#3.2

def evenOrOdd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

print(evenOrOdd(4))


# 4

# 4.1

numbers = [1, 2, 3, 4, 5]

def sumwithloop(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sumwithloop(numbers))

# 5

# 5.1

def duplicatedlist(numbers):
    newlist = []
    for num in numbers:
        newlist.extend([num, num])
    return newlist

print(duplicatedlist(numbers))

# 5.2

# the function's variable should be a single letter like x or a not a string like "num"
def square(x):
    return x * x

print(square(5))