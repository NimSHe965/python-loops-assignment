#Task 3: Performance Comparison
import numpy as np
import time

# NumPy array with numbers 1 to 50,000
np_array = np.arange(1, 50001)

# Python list with numbers 1 to 50,000
py_list = list(range(1, 50001))
start_time = time.time()
numpy_sum = np.sum(np_array)
end_time = time.time()

# Calculate how long it took
numpy_time = end_time - start_time

start_time = time.time()
python_sum = sum(py_list)
end_time = time.time()

# Calculate how long it took
python_time = end_time - start_time

print("NumPy sum:", numpy_sum)
print("Python sum:", python_sum)

# Format time to 4 decimal places using f-strings
print(f"NumPy time: {numpy_time:.4f} seconds")
print(f"Python time: {python_time:.4f} seconds")

# (We divide Python time by NumPy time to see the difference)
speed_difference = python_time / numpy_time

print(f"NumPy is {speed_difference:.1f}x faster")