# -*- coding: utf-8 -*-
# @Author: razor87
# @Date:   2019-06-24 12:18:25
# @Last Modified by:   razor87
# @Last Modified time: 2020-01-31 20:25:58
import io
import sys


# 'r'  open for reading (default)
# 'w'  open for writing, truncating the file first
# 'x'  open for exclusive creation, failing if the file already exists
# 'a'  open for writing, appending to the end of the file if it exists
# 'b'  binary mode
# 't'  text mode (default)
# '+'  open a disk file for updating (reading and writing)




sys.stdin
sys.stdin.read()
sys.stdin.readline()
sys.stdin.readlines()



sys.stdin = io.StringIO("1\n2\n3\n4\n5\n6\n7\n8\n9")
sys.stdin.getvalue()
# '1\n2\n3\n4\n5\n6\n7\n8\n9'


print(data, file=file, flush=True)


f = open('data.txt')
first, second, *rest, last = f.readlines()
f.close()



with open('input00.txt') as f:
    _, arr = f.readline(), tuple(f.readline().split())

with open("input07.txt") as f:
    _, n, m = (f.readline(), map(int, f.readline().split()),
               ({*map(int, f.readline().split())} for _ in range(2)))


with open('mydata.txt') as fp:
    for line in iter(fp.readline, ''):
        process_line(line)





with open(file) as f:
    file.write()
    file.tell()
    file.read()
    file.seek(0)
    file.readline()
    file.readlines()

file.writelines()



with open("/path/to/file") as f:
    for line in f:
        print(line)

f = open("/path/tofile", 'w')
for e in aList:
    f.write(e + "\n")
f.close()


def f_open(filename='input.txt', mock=False):
    try:
        with open(filename) as f:
            inp = f
    except FileNotFoundError:
        import sys
        if mock:
            import io
            sys.stdin = io.StringIO(mock)
        inp = sys.stdin
    return inp


fake = '2\nA\nB : A\n1\nC C'
print(f_open(mock=fake).read())



def download(url, log=print):
    log(f'Downloading {url}')
    # ...

def mock_print(message):
    mock_print.last_message = message

download('resource', mock_print)
# assert 'Downloading resource' == mock_print.last_message


def download_(url, stream=None):
    print(f'Downloading {url}', file=stream)
    # ...

memory_buffer = io.StringIO()
download_('app.js', memory_buffer)
download_('style.css', memory_buffer)
memory_buffer.getvalue()
# 'Downloading app.js\nDownloading style.css\n'

