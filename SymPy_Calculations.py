import sympy as sp # Importing the sympy library


# 1) Create a row matrix 𝐗 with the sequence of even numbers from 2 to 8 as entries
X = sp.Matrix([[2, 4, 6, 8]]) # Create a row matrix X

# (a) Find the matrix resulting from 𝐀 = 𝐗𝑻𝐗
A = X.T * X # Compute A = X^T * X
print("Matrix A:\n")
sp.pprint(A)

# (b) Show why matrix 𝐀 is symmetric
print("\nTranspose of matrix A:\n")
sp.pprint(A.T) # Print the transpose of matrix A
print("\nIs matrix A symmetric?", A == A.T) # Check if A is symmetric using boolean comparison

# (c) Calculate the determinant of matrix 𝐀
determint_A = A.det() # Find the determinant of A
print("\n|A| = det(A) =", determint_A)



# 2) Consider matrix 𝐁 shown below. Answer the following questions:

#(b) Calculate the determinant of matrix 𝐀
B = sp.Matrix([
    [0, 1, 0, -2, 1],
    [1, 0, 3, 1, 1],
    [1, -1, 1, 1, 1],
    [2, 2, 1, 0, 1],
    [3, 1, 1, 1, 2]
])

print("\nMatrix B:\n")
sp.pprint(B)

determint_B = B.det()  # Find the determinant of A
print("\n|A| = det(A) =", determint_B)
print("")



# 3) Consider matrix 𝐂 shown below. Answer the following questions:
t = sp.Symbol('t') # Define a symbolic variable t

C = sp.Matrix([ # Create matrix C with symbolic entries
    [t, -t, 1],
    [t - 1, t, 2],
    [-1, -2*t, 1]
])

print("\nMatrix C:\n")
sp.pprint(C)

determinant_C = C.det() # Calculate the determinant of matrix C
print("\n|C| = det(C) =", determinant_C)

# Solve for when det = 0
solved_det_C = sp.solve(determinant_C, t) # Find the values of t for which the determinant is zero
print("Matrix is not invertible when t =", solved_det_C)