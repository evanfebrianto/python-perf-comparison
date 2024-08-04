def sum_of_squares_cython(int n):
    cdef long total = 0
    cdef int i
    for i in range(n):
        total += i * i
    return total
