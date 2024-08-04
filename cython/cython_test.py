import time
from sum_of_squares import sum_of_squares_cython

n = 10**7
start_time = time.time()
result = sum_of_squares_cython(n)
end_time = time.time()

print("Result:", result)
print("Execution Time (Cython):", end_time - start_time, "seconds")
