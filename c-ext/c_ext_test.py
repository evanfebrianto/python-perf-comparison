import time
from sumofsquares import sum_of_squares_c

n = 10**7
start_time = time.time()
result = sum_of_squares_c(n)
end_time = time.time()

print("Result:", result)
print("Execution Time (C Extension):", end_time - start_time, "seconds")
