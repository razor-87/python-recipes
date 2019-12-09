# -*- coding: utf-8 -*-
# @Author: razor87
# @Date:   2019-09-29 19:29:38
# @Last Modified by:   razor87
# @Last Modified time: 2019-12-05 19:21:57
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


filename, file_extension = os.path.splitext('/path/to/somefile.ext')



from pathlib import Path

dataset = 'wiki_images'
datasets_root = Path('/path/to/datasets/')

train_path = datasets_root / dataset / 'train'
test_path = datasets_root / dataset / 'test'

for image_path in train_path.iterdir():
    with image_path.open() as f:
        ...


<bool> = <Path>.exists()
<bool> = <Path>.is_file()
<bool> = <Path>.is_dir()
<iter> = <Path>.iterdir()           # Returns dir contents as Path objects.
<iter> = <Path>.glob('<pattern>')   # Returns Paths matching the wildcard pattern.
<str>  = str(<Path>)                # Path as a string.
<str>  = <Path>.name                # Final component.
<str>  = <Path>.stem                # Final component without extension.
<str>  = <Path>.suffix              # Final component's extension.
<tup.> = <Path>.parts               # All components as strings.
<Path> = <Path>.resolve()           # Returns absolute path without symlinks.
<Path> = <Path>.parent              # Returns path without final component.
<file> = open(<Path>)               # Opens the file and returns a file object.


p.exists()
p.is_dir()
p.parts
p.with_name('sibling.png') # only change the name, but keep the folder
p.with_suffix('.jpg') # only change the extension, but keep the folder and the name
p.chmod(mode)
p.rmdir()



p_text = Path('my_text_file')
p_text.write_text('Text file contents')
# 18
p_text.read_text()
# 'Text file contents'
p_binary = Path('my_binary_file')
p_binary.write_bytes(b'Binary file contents')
# 20
p_binary.read_bytes()
# b'Binary file contents'


cur_path = Path(".")
FILE_PATTERN = "*.txt"
path_list = cur_path.glob(FILE_PATTERN)
print(list(path_list))



import glob
found_images = glob.glob('/path/**/*.jpg', recursive=True)
# A better option is to use pathlib in python3 (minus one import!):
found_images = Path('/path/').glob('**/*.jpg')
