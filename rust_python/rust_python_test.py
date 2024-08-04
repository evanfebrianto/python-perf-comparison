import time
from rust_python import sum_of_squares_rust

n = 10**7
start_time = time.time()

try:
    result = sum_of_squares_rust(n)
    print("Result:", result)
except OverflowError as e:
    print(f"Error: {e}")

end_time = time.time()
print("Execution Time (Rust Extension):", end_time - start_time, "seconds")
