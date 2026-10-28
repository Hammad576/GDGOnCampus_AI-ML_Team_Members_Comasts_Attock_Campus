# %% Imports
import numpy as np
import numpy.ma as ma

# ==========================================
# %% Assignment 1: Array Creation and Manipulation
# ==========================================

# 1. 5x5 random integers (1 to 20), replace 3rd column with 1
arr1_1 = np.random.randint(1, 21, size=(5, 5))
print("Assignment 1.1 - Original:\n", arr1_1)
arr1_1[:, 2] = 1
print("Assignment 1.1 - 3rd column replaced with 1:\n", arr1_1)

# 2. 4x4 array (1 to 16), replace diagonal with 0
arr1_2 = np.arange(1, 17).reshape(4, 4)
print("\nAssignment 1.2 - Original:\n", arr1_2)
np.fill_diagonal(arr1_2, 0)
print("Assignment 1.2 - Diagonal replaced with 0:\n", arr1_2)


# ==========================================
# %% Assignment 2: Array Indexing and Slicing
# ==========================================

# 1. 6x6 array (1 to 36), extract rows 3-5 and cols 2-4
arr2_1 = np.arange(1, 37).reshape(6, 6)
sub_arr2_1 = arr2_1[2:5, 1:4]
print("\nAssignment 2.1 - Sub-array (rows 3-5, cols 2-4):\n", sub_arr2_1)

# 2. 5x5 array, extract border elements
arr2_2 = np.random.randint(1, 50, size=(5, 5))
print("\nAssignment 2.2 - Original 5x5:\n", arr2_2)
top = arr2_2[0, :]
bottom = arr2_2[-1, :]
left = arr2_2[1:-1, 0]
right = arr2_2[1:-1, -1]
border_elements = np.concatenate([top, right, bottom[::-1], left[::-1]])
print("Assignment 2.2 - Border elements:\n", border_elements)


# ==========================================
# %% Assignment 3: Array Operations
# ==========================================

# 1. Two 3x4 arrays: addition, subtraction, multiplication, division
a = np.random.randint(1, 10, size=(3, 4))
b = np.random.randint(1, 10, size=(3, 4))
print("\nAssignment 3.1 - Array A:\n", a)
print("Assignment 3.1 - Array B:\n", b)
print("Addition:\n", a + b)
print("Subtraction:\n", a - b)
print("Multiplication:\n", a * b)
print("Division:\n", np.round(a / b, 2))

# 2. 4x4 array (1 to 16), row-wise and column-wise sum
arr3_2 = np.arange(1, 17).reshape(4, 4)
print("\nAssignment 3.2 - Matrix:\n", arr3_2)
print("Row-wise sum:", np.sum(arr3_2, axis=1))
print("Column-wise sum:", np.sum(arr3_2, axis=0))


# ==========================================
# %% Assignment 4: Statistical Operations
# ==========================================

# 1. 5x5 array: mean, median, standard deviation, variance
arr4_1 = np.random.randint(1, 100, size=(5, 5))
print("\nAssignment 4.1 - Array:\n", arr4_1)
print("Mean:              ", np.mean(arr4_1))
print("Median:            ", np.median(arr4_1))
print("Standard Deviation:", round(np.std(arr4_1), 2))
print("Variance:          ", round(np.var(arr4_1), 2))

# 2. 3x3 array (1 to 9), normalized (mean=0, std=1)
arr4_2 = np.arange(1, 10, dtype=float).reshape(3, 3)
normalized = (arr4_2 - np.mean(arr4_2)) / np.std(arr4_2)
print("\nAssignment 4.2 - Normalized Array:\n", np.round(normalized, 2))


# ==========================================
# %% Assignment 5: Broadcasting
# ==========================================

# 1. Add 1D array (3,) to each row of 2D array (3, 3)
arr5_1 = np.random.randint(1, 10, size=(3, 3))
row_vec = np.array([10, 20, 30])
print("\nAssignment 5.1 - 2D Array:\n", arr5_1)
print("Assignment 5.1 - Row Vector to add:\n", row_vec)
print("Result (added to each row):\n", arr5_1 + row_vec)

# 2. Subtract 1D array (4,) from each column of 2D array (4, 4)
arr5_2 = np.random.randint(1, 20, size=(4, 4))
col_vec = np.array([1, 2, 3, 4])
res5_2 = arr5_2 - col_vec  # subtract each column value from the matching column
print("\nAssignment 5.2 - 2D Array:\n", arr5_2)
print("Assignment 5.2 - Subtracted from each column:\n", res5_2)


# ==========================================
# %% Assignment 6: Linear Algebra
# ==========================================

# 1. 3x3 matrix: determinant, inverse, eigenvalues
mat6_1 = np.array([[2, 1, 1], 
                   [1, 3, 2], 
                   [1, 0, 0]], dtype=float)
print("\nAssignment 6.1 - Matrix:\n", mat6_1)
print("Determinant:", round(np.linalg.det(mat6_1), 2))
print("Inverse:\n", np.round(np.linalg.inv(mat6_1), 2))
eigenvalues, _ = np.linalg.eig(mat6_1)
print("Eigenvalues:", np.round(eigenvalues, 2))

# 2. Matrix multiplication (2, 3) @ (3, 2)
mat_a = np.random.randint(1, 5, size=(2, 3))
mat_b = np.random.randint(1, 5, size=(3, 2))
print("\nAssignment 6.2 - Matrix A (2x3):\n", mat_a)
print("Assignment 6.2 - Matrix B (3x2):\n", mat_b)
print("Matrix Multiplication (A @ B):\n", mat_a @ mat_b)


# ==========================================
# %% Assignment 7: Advanced Array Manipulation
# ==========================================

# 1. 3x3 array reshaped to (1, 9) and (9, 1)
arr7_1 = np.arange(1, 10).reshape(3, 3)
print("\nAssignment 7.1 - Original (3, 3):\n", arr7_1)
print("Reshaped to (1, 9):\n", arr7_1.reshape(1, 9))
print("Reshaped to (9, 1):\n", arr7_1.reshape(9, 1))

# 2. 5x5 array: flatten and reshape back to (5, 5)
arr7_2 = np.random.randint(1, 50, size=(5, 5))
flattened = arr7_2.flatten()
restored = flattened.reshape(5, 5)
print("\nAssignment 7.2 - Flattened Shape:", flattened.shape)
print("Assignment 7.2 - Restored Shape:", restored.shape)
print("Is restored equal to original?", np.array_equal(arr7_2, restored))


# ==========================================
# %% Assignment 8: Fancy Indexing and Boolean Indexing
# ==========================================

# 1. Extract 4 corner elements of a 5x5 array
arr8_1 = np.random.randint(1, 50, size=(5, 5))
print("\nAssignment 8.1 - 5x5 Array:\n", arr8_1)
corners = arr8_1[[0, 0, -1, -1], [0, -1, 0, -1]]
print("Corners [top-left, top-right, bottom-left, bottom-right]:", corners)

# 2. Set all elements greater than 10 to 10
arr8_2 = np.random.randint(1, 25, size=(4, 4))
print("\nAssignment 8.2 - Before capping:\n", arr8_2)
arr8_2[arr8_2 > 10] = 10
print("Assignment 8.2 - After capping (>10 set to 10):\n", arr8_2)


# ==========================================
# %% Assignment 9: Structured Arrays
# ==========================================

# 1. Structured array: name, age, weight (sorted by age)
dtype_person = [('name', 'U20'), ('age', int), ('weight', float)]
data_person = [('Alice', 25, 55.4), ('Bob', 30, 72.1), ('Charlie', 22, 68.0), ('Diana', 28, 59.5)]
people = np.array(data_person, dtype=dtype_person)
print("\nAssignment 9.1 - Sorted by age:\n", np.sort(people, order='age'))

# 2. Structured array: (x, y) coordinates & Euclidean distance
dtype_point = [('x', int), ('y', int)]
data_points = [(0, 0), (3, 4), (6, 8), (1, 1)]
points = np.array(data_points, dtype=dtype_point)
coords = np.column_stack((points['x'], points['y']))
diff = coords[:, np.newaxis, :] - coords[np.newaxis, :, :]
dist_matrix = np.sqrt(np.sum(diff**2, axis=-1))
print("\nAssignment 9.2 - Points:\n", points)
print("Pairwise Euclidean Distances:\n", np.round(dist_matrix, 2))


# ==========================================
# %% Assignment 10: Masked Arrays
# ==========================================

# 1. Mask elements > 10 in 4x4 array and compute unmasked sum
raw10_1 = np.random.randint(1, 20, size=(4, 4))
masked10_1 = ma.masked_greater(raw10_1, 10)
print("\nAssignment 10.1 - Masked Array (> 10 hidden):\n", masked10_1)
print("Sum of unmasked elements:", masked10_1.sum())

# 2. Mask diagonal of 3x3 array and replace with unmasked mean
raw10_2 = np.random.randint(1, 20, size=(3, 3)).astype(float)
diag_mask = np.eye(3, dtype=bool)
masked10_2 = ma.masked_array(raw10_2, mask=diag_mask)
unmasked_mean = masked10_2.mean()
filled10_2 = masked10_2.filled(unmasked_mean)

print("\nAssignment 10.2 - Original:\n", raw10_2)
print("Assignment 10.2 - Diagonal Masked:\n", masked10_2)
print("Unmasked Mean:", round(unmasked_mean, 2))
print("Array with diagonal filled with unmasked mean:\n", np.round(filled10_2, 2))