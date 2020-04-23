# https://stackoverflow.com/questions/845058/how-to-get-line-count-of-a-large-file-cheaply-in-python
from itertools import (takewhile,repeat)
def rawincount(filename):
    f = open(filename, 'rb')
    bufgen = takewhile(lambda x: x, (f.raw.read(1024*1024) for _ in repeat(None)))
    return sum( buf.count(b'\n') for buf in bufgen )
