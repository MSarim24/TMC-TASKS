import numpy as np

# Python list vs NumPy array
py_list = [1, 2, 3]
num_array = np.array([1, 2, 3], dtype=np.float64)

print("--- 1. Metadata & Types ---")
print(f"Array Data Type (dtype): {num_array.dtype}")
print(f"Array Dimensions (ndim): {num_array.ndim}")

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D Matrix Shape: {matrix.shape}")  

print("--- 2. Array Manipulation ---")


zeros_arr = np.zeros((2, 4))       
range_arr = np.arange(0, 10, 2)   


grid = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(f"Specific element (row 1, col 2): {grid[0, 1]}") 
print(f"Slice (First 2 rows, last 2 cols):\n{grid[:2, 1:]}")

# Boolean Masking
data = np.array([12, 45, 78, 23, 56])
mask = data > 40
print(f"Boolean Mask result: {mask}")
print(f"Filtered Data: {data[mask]}") 

print("--- 3. Math & Broadcasting ---")

prices = np.array([10.0, 25.0, 50.0])
discounted_prices = prices * 0.9 
print(f"Vectorized Discount (-10%): {discounted_prices}")

matrix_3x3 = np.ones((3, 3)) * 10
row_vector = np.array([1, 2, 3])

broadcasted_sum = matrix_3x3 + row_vector
print(f"Broadcasting Result:\n{broadcasted_sum}")

print("--- 4. Structural Changes & Aggregations ---")

stats_matrix = np.array([[1, 2], [3, 4], [5, 6]])

print(f"Global Sum: {np.sum(stats_matrix)}")
print(f"Column-wise Sum (axis=0): {np.sum(stats_matrix, axis=0)}")
print(f"Row-wise Mean (axis=1): {np.mean(stats_matrix, axis=1)}")

flat_arr = np.arange(12) 
reshaped_matrix = flat_arr.reshape(4, -1) 
print(f"Reshaped Matrix (4x3):\n{reshaped_matrix}")

# Stacking
a = np.array([1, 2])
b = np.array([3, 4])
print(f"Vertical Stack:\n{np.vstack((a, b))}")
print(f"Horizontal Stack: {np.hstack((a, b))}")

print("--- 5. Math, Randomization, & Linear Algebra ---")

# Linear spacing split points
lin_spaced = np.linspace(0, 1, 5) 
print(f"5 Evenly spaced points between 0 and 1: {lin_spaced}")


rng = np.random.default_rng(seed=42) 
random_matrix = rng.random((2, 2))
print(f"Random floats matrix:\n{random_matrix}")

# Linear Algebra Matrix Multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 2]])

element_wise = A * B   
dot_product = A @ B    

print(f"Element-wise multiplication product:\n{element_wise}")
print(f"Linear Algebra Matrix dot product (@):\n{dot_product}")
print(f"Transpose of Matrix A:\n{A.T}")