import struct
print struct.calcsize("P")*8

import itertools

arr = [[1,2,3,4],
       [12,13,14,5],
       [11,16,15,6],
       [10,9,8,7]]

def transpose_and_yield_top(arr):
    while arr:
        yield arr[0]
        arr = list(reversed(zip(*arr[1:])))

print list(itertools.chain(*transpose_and_yield_top(arr)))
