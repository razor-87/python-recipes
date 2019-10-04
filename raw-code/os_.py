# -*- coding: utf-8 -*-
import os
for key in os.environ:
    print(key, ':', os.environ[key])
for key in os.environ:
    print('{:>30} {:<4} {:}'.format(key, ':', os.environ[key]))


# os MODULE FUNCTION WHAT IT DOES
os.chdir(path)  # Changes the current working directory to path.
os.getcwd()  # Returns the path of the current working directory.
os.listdir(path)  # Returns a list of the names in directory named path.
os.mkdir(path)  # Creates a new directory named path and places it in the current working directory.
os.remove(path)  # Removes the file named path from the current working directory.
os.rename(old, new)  # Renames the file or directory named old to new.
os.rmdir(path)  # Removes the directory named path from the current working directory

# os.path MODULE FUNCTION WHAT IT DOES
os.exists(path)  # Returns True if path exists and False otherwise.
os.isdir(path)  # Returns True if path names a directory and False otherwise.
os.isfile(path)  # Returns True if path names a file and False otherwise.
os.getsize(path)  # Returns the size of the object names by path in bytes.


os._exit()


# Files
import os
currentDirectoryPath = os.getcwd()
listOfFileNames = os.listdir(currentDirectoryPath)
for name in listOfFileNames:
    if '.py' in name:
        print(name)
