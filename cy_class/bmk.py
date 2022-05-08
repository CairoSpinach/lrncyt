from typing import Dict

import integrate
from basic import Fun, SinSq
from math import sin

class MyF(Fun):
    def eval(self, x):
        return super().eval(x / 2.)

class MyG(Fun):
    def eval(self, x):
        return sin(x ** 2)

class BenchmarkInt:
    def __init__(self, fmap: Dict[str, Fun], g):
        self.fmap = fmap
        self.integrate = g

    def eval_on(self, a, b, N=100_000):
        for fname, f in self.fmap.items():
            with timeit(fname):
                self.integrate(f, a, b, N)


def py_integrate(f: Fun, a, b, N):
    if f is None:
        raise ValueError("f cannot be None")
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f.eval(a + i * dx)
    return s * dx


bmk = BenchmarkInt({
    'SinSq': SinSq(),
    'MyF': MyF(),
    'MyG (py sinsq)': MyG(),
}, integrate.integrate)

bmk.eval_on(-1, 10, 5_000_000)

bmk2 = BenchmarkInt({
    'SinSq': SinSq(),
    'MyF': MyF(),
    'MyG (py sinsq)': MyG(),
}, py_integrate)

bmk2.eval_on(-1, 10, 5_000_000)

### output
# SinSq used 0.20 s
# MyF used 1.22 s
# MyG (py sinsq) used 1.37 s
# SinSq used 0.91 s
# MyF used 1.74 s
# MyG (py sinsq) used 1.83 s