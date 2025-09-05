#using all numpy functions to carry each task one by one
import numpy as np

matrix = np.random.randint(1, 101, size=(5, 5))

print("Matrix:")
print(matrix)

max_val = np.max(matrix)
min_val = np.min(matrix)
mean_val = np.mean(matrix)

print(f"\nMaximum value: {max_val}")
print(f"Minimum value: {min_val}")
print(f"Mean value: {mean_val:.2f}")

normalized_matrix = (matrix - min_val) / (max_val - min_val)

print("\nNormalized matrix:")
print(normalized_matrix)

flattened_array = normalized_matrix.flatten()

sorted_array = np.sort(flattened_array)

print("\nSorted flattened array:")
print(sorted_array)