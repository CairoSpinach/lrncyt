cdef class Fun:
    cpdef double eval(self, double x) except *

cdef class SinSq(Fun):
    cpdef double eval(self, double x) except *

