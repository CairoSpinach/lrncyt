# from basic cimport Fun, SinSq
from libc.math cimport sin


cdef class Fun:

    cpdef double eval(self, double x) except *:
        return 0


cdef class SinSq(Fun):

    cpdef double eval(self, double x) except *:
        return sin(x ** 2)

# cdef class SS(Fun):
#     cdef double eval(self, double x) except *:
#         return sin(x ** 2)