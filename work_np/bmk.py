from clipping import compute, compute2
from util import timeit

import numpy as np

a1 = np.random.randint(-3, 5, size=(2000, 2500))
a2 = np.random.randint(-3, 5, size=(2000, 2500))
a, b, c = 4, 2, 9

with timeit(f'compute on array of {a1.shape}'):
    res = compute(a1, a2, a, b, c)   # used 0.04 s

print(f'res shape = {res.shape}, sum = {res.sum()}')

with timeit(f'compute2 on array of {a1.shape}'):
    res2 = compute2(a1, a2, a, b, c)  # used 3.11 s

print(f'res2 shape = {res2.shape}, sum = {res2.sum()}')
