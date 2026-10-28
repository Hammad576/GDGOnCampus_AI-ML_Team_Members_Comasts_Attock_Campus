import numpy as np

#------------------------------------------------------------
#----------------Task 1: Create a NumPy array----------------
#------------------------------------------------------------

# Create a 5x5 array with random integers between 1 and 20
arr1 = np.random.randint(1, 21, size=(5, 5))
print("Original Array:",arr1)

# Replace all elements in the third column with 1
arr1[:, 2] = 1

print("Modified Array:",arr1)

#---------------------Part 2-----------------------------------
arr2 = np.random.randint(1, 17, size=(4, 4)) 
print("Original Array:",arr2)

np.fill_diagonal(arr2, 0)
print("Modified Array:",arr2)


#------------------------------------------------------------
#----------------Task 2: Silicing a NumPy array--------------
#------------------------------------------------------------

arr3 = np.arange(1, 37).reshape(6, 6)
print("Array:\n", arr3)

# Rows 3-5 -> indices 2:5, Columns 2-4 -> indices 1:4
sub_array = arr3[2:5, 1:4]
print("Sub-array:\n", sub_array)


#--------------------Part 2-----------------------------------
arr4 = np.random.randint(1, 50, size=(5, 5))
print("Array:\n", arr4)

# Combine top row, bottom row, left column , right column
border = np.concatenate([
    arr4[0, :],        
    arr4[-1, :],       
    arr4[1:-1, 0],     
    arr4[1:-1, -1]     
])
print("Border elements:", border)


#------------------------------------------------------------
#-----------------Task 3: Array Operations-------------------
#------------------------------------------------------------
arr5 = np.random.randint(1, 21, size=(3, 4))
arr6 = np.random.randint(1, 21, size=(3, 4))
print("Array 5:\n", arr5)
print("Array 6:\n", arr6)

# Element-wise addition
print("Sum Array:\n", arr5 + arr6)
# Element-wise multiplication
print("Product Array:\n", arr5 * arr6)
# Element-wise subtraction
print("Difference Array:\n", arr5 - arr6)
# Element-wise division
print("Division Array:\n", arr5 / arr6)


#--------------------Part 2-----------------------------------
arr7 = np.random.randint(1, 17, size=(4, 4))
print("Array 7:\n", arr7)
# Calculate the sum of each row
print("Row sums:", np.sum(arr7, axis=1))
# Calculate the sum of each column
print("Column sums:", np.sum(arr7, axis=0))

# Calculate the product of each row
print("Row products:", np.prod(arr7, axis=1))
# Calculate the product of each column
print("Column products:", np.prod(arr7, axis=0))



#---------------------------------------------------------------
#----------------Task 4: Statistical Operations ----------------
#---------------------------------------------------------------
arr8 = np.random.randint(1, 101, size=(5, 5))
print("Array 8:\n", arr8)
# Calculate mean, median, standard deviation, and variance
print("Mean of Array 8:", np.mean(arr8))
print("Median of Array 8:", np.median(arr8))
print("Standard Deviation of Array 8:", np.std(arr8))
print("Variance of Array 8:", np.var(arr8))


#--------------------Part 2-----------------------------------
arr9 = np.random.randint(1, 10, size=(3, 3))
print("Array 9:\n", arr9)
#Normalize the array to have values between 0 and 1
normalized = (arr9 - np.mean(arr9)) / np.std(arr9)
print("Normalized Array:\n", normalized)

print("Mean of Normalized Array:", np.mean(normalized))
print("Standard Deviation of Normalized Array:", np.std(normalized))


#------------------------------------------------------------------
#---------------------Task 5: Broadcasting-------------------------
#------------------------------------------------------------------
arr10 = np.random.randint(1, 11, size=(3, 3))
print("Array 10:\n", arr10)

# Add a 1D array to each row of the 2D array of shape(3, 1)
arr11 = np.random.randint(1, 11, size=(3, 1))
print("Array 11:\n", arr11)
result = arr10 + arr11
print("Result of Broadcasting:\n", result)

#--------------------Part 2-----------------------------------
arr11 = np.random.randint(1, 17, size=(4, 4))
print("Array 11:\n", arr11)
# Subtract a 1D array from each column of the 2D array of shape(4, 1)
arr12 = np.random.randint(1, 17, size=(4,))
print("Array 12:\n", arr12)
result = arr11 - arr12
print("Result of Broadcasting:\n", result)


#---------------------------------------------------------------
#---------------------Task 6: Linear algebra--------------------
#---------------------------------------------------------------
arr12 = np.random.randint(1, 10, size=(3, 3))
print("Array 12:\n", arr12)
# Calculate the determinant of the array
print("Determinant of Array 12:", np.linalg.det(arr12))
# Calculate the inverse of the array
if np.linalg.det(arr12) != 0:
    print("Inverse of Array 12:\n", np.linalg.inv(arr12))
else:
    print("Array 12 is singular and cannot be inverted.")

#Calculate the eigenvalues and eigenvectors of the array
print("Eigenvalues of Array 12:", np.linalg.eigvals(arr12))


#--------------------Part 2-----------------------------------
arr13 = np.random.randint(1, 10, size=(2, 3))
print("Array 13:\n", arr13)
arr14 = np.random.randint(1, 10, size=(3, 2))
print("Array 14:\n", arr14)

# Perform matrix multiplication between two arrays
result = np.dot(arr13, arr14)
print("Result of Matrix Multiplication:\n", result)



#---------------------------------------------------------------
#----------------Task 7: Advanced array Manipulation------------
#---------------------------------------------------------------

#Array of shape (3,3) filled with 1 to 9
arr15 = np.arange(1, 10).reshape(3, 3)
print("Array 15:\n", arr15)
#reshape array as (9,1)
arr15_reshaped = arr15.reshape(9, 1)
print("Reshaped Array 15:\n", arr15_reshaped)


#--------------------Part 2-----------------------------------
arr16 = np.random.randint(1, 20, size=(5, 5))
print("Array 16:\n", arr16)
#Flatten the array and reshape back the array
arr16_flattened = arr16.flatten()
print("Flattened Array 16:\n", arr16_flattened)
arr16_reshaped = arr16_flattened.reshape(5, 5)
print("Reshaped Array 16:\n", arr16_reshaped)



#---------------------------------------------------------------
#--------------Task 8: Fancy and Boolean Indexing---------------
#---------------------------------------------------------------
arr17 = np.random.randint(1, 21, size=(5, 5))
print("Array 17:\n", arr17)
#Extract elements from corner by fancy indexing
corners = arr17[[0, 0, 4, 4], [0, 4, 0, 4]]
print("Corner elements:", corners)

#--------------------Part 2-----------------------------------
arr18 = np.random.randint(2, 21, size=(4, 4))
print("Array 18:\n", arr18)
#Extract elements greater than 10 using boolean indexing
elements_greater_than_10 = arr18[arr18 > 10]
print("Elements greater than 10:", elements_greater_than_10)



#---------------------------------------------------------------
#----------------Task 9: Structured array-----------------------
#---------------------------------------------------------------

#Array of name, age and weight of 3 people
arr19 = np.array([('Alice', 25, 55.2), ('Bob', 30, 70.7), ('Charlie', 35, 80.0)], 
                  dtype=[('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])
print("Array 19:\n", arr19)
#Sort by age
sorted_by_age = np.sort(arr19, order='age')
print("Sorted by age:\n", sorted_by_age)

#--------------------Part 2-----------------------------------
points = np.array(
    [(0, 0), (3, 4), (6, 8), (9, 12)],
    dtype=[('x', 'i4'), ('y', 'i4')]
)
print("Points:\n", points)

coordinates = np.column_stack((points['x'], points['y']))
differences = np.diff(coordinates, axis=0)
distances = np.sqrt(np.sum(differences ** 2, axis=1))

print("Distances between consecutive points:", distances)



#---------------------------------------------------------------
#----------------Task 10: Masked Arrays-------------------------
#---------------------------------------------------------------
arr20 = np.random.randint(1, 21, size=(4, 4))
print("Array 20:\n", arr20)
#Create a masked array where elements greater than 10 are masked
masked_arr = np.ma.masked_greater(arr20, 10)
print("Masked Array:\n", masked_arr)
#Sum of unmasked elements
print("Sum of unmasked elements:", masked_arr.sum())

#--------------------Part 2-----------------------------------
arr21 = np.random.randint(1, 21, size=(3, 3))
print("Array 21:\n", arr21)
#Masked the diagonal elements of the array
masked_diagonal = np.ma.masked_array(arr21, mask=np.eye(3, dtype=bool))
print("Masked Diagonal Array:\n", masked_diagonal)
#Replace the masked elements with the mean of the unmasked elements
mean_unmasked = masked_diagonal.mean()
masked_diagonal_filled = masked_diagonal.filled(mean_unmasked)
print("Masked Diagonal Array with masked elements replaced by mean:\n", masked_diagonal_filled)