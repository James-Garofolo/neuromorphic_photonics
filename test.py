import numpy as np
import time as t

a = [[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]]

for b in a:
    for c in b:
        c.append(0)

print(a)