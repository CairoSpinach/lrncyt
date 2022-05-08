from libc.math cimport pow

cdef double square_and_add(double x):
    """ compute x**2 + x as double.
       cdef function that can be called from within cython but not from python directly  
    """
    return pow(x, 2.) + x


cpdef print_res(double x):
    print("({} ^ 2 + {} - {}".format(x, x, square_and_add(x)))



