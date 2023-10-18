import numpy as np

# Create an array
array = np.array([1, 7, 13, 105])

# Determine the size of memory occupied by the array
memory_size = array.nbytes

print("Array:", array)
print("Memory size occupied by the array:", memory_size, "bytes")