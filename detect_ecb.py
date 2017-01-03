from binascii import a2b_hex
from itertools import combinations, izip
import os

def is_ecb_encoded(data, block_size):
    myrange = range(0, len(data), block_size)
    inds = combinations(zip(myrange, myrange[1:]), 2)
    return any(data[i1:i2] == data[j1:j2] for (i1, i2), (j1, j2) in inds)

with open((os.path.dirname(__file__) + 'ch8.txt')) as fobj:
    lines = (line.rstrip() for line in fobj)
    # lines = (a2b_hex(line) for line in lines)
    lines = (line for line in lines if is_ecb_encoded(line, 16))
    print '\n'.join(lines)
    # print (lines)