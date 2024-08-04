import time

def sum_of_squares(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

# Measure execution time
n = 10**7
start_time = time.time()
result = sum_of_squares(n)
end_time = time.time()

print("Result:", result)
print("Execution Time (Normal Python):", end_time - start_time, "seconds")
