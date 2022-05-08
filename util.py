import time
from contextlib import contextmanager


@contextmanager
def timeit(msg):
    t0 = time.time()
    yield
    dt = time.time() - t0
    print(msg, f'used {dt:.2f} s')
