import cython
from Cython import declare


a_global_variable = declare(cython.int, 42)   # wouldn't work

def func(f: cython.float):
    i: cython.int = 10
    # f: cython.float = 2.5
    g: cython.int[4] = [1, 2, 3, 4]
    h: cython.p_float = cython.address(f)
    if h[0] == 2.5:
        g[2] = 0
    else:
        g[2] = -a_global_variable
    return g


