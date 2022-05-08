from basic cimport Fun, SinSq

def integrate(Fun f, double a, double b, int N):
    cdef int i
    cdef double s, dx
    if f is None:
        raise ValueError("f cannot be None")

    s = 0
    dx = (b - a) / N

    for i in range(N):
        s += f.eval(a + i * dx)

    return s * dx

