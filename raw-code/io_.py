# -*- coding: utf-8 -*-
# @Author: razor87
# @Date:   2019-06-24 12:18:25
# @Last Modified by:   razor87
# @Last Modified time: 2020-02-11 19:08:41
"""
'r'  open for reading (default)
'w'  open for writing, truncating the file first
'x'  open for exclusive creation, failing if the file already exists
'a'  open for writing, appending to the end of the file if it exists
'b'  binary mode
't'  text mode (default)
'+'  open a disk file for updating (reading and writing)
"""
import io
import sys


sys.stdin.read()
sys.stdin.readline()
sys.stdin.readlines()

sys.stdin = io.StringIO("1\n2\n3\n4\n5\n6\n7\n8\n9")
sys.stdin.getvalue()
# '1\n2\n3\n4\n5\n6\n7\n8\n9'


with open('mydata.txt') as fp:
    for line in iter(fp.readline, ''):
        process_line(line)

f = open('/etc/passwd')
for chunk in iter(lambda: f.read(10), ''):
    n = sys.stdout.write(chunk)


def download(url, log=print):
    log(f'Downloading {url}')
    # ...

def mock_print(message):
    mock_print.last_message = message

download('resource', mock_print)
# assert 'Downloading resource' == mock_print.last_message


def download_(url, stream=None):
    """
    >>> memory_buffer = io.StringIO()
    >>> download_('app.js', memory_buffer)
    >>> download_('style.css', memory_buffer)
    >>> memory_buffer.getvalue()
    'Downloading app.js\nDownloading style.css\n'
    """
    print(f'Downloading {url}', file=stream)


def reader_chunks(s, chunksize=8192):
    for chunk in iter(lambda: s.recv(chunksize), b''):
        process_data(data)


def f_open(filename='input.txt', mock=False):
    """
    >>> fake = '2\nA\nB : A\n1\nC C'
    >>> f_open(mock=fake).read()
    '2\nA\nB : A\n1\nC C'
    """
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
