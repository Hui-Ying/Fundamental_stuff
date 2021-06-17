# Class matrix calculation: create a class for 3 functions.
# Function 1: save a random matrix in a txt file.
# Function 2: get the inner product of m random matrices, one of the matrices is from Function 1
# Function 3: Read the results of the matrix from Function 1 and Function 2.

#l*l rondom matrix
#m:  # of matrices
# libraries 
import numpy as np
class matrix_calculation:
    def __init__(self, l, m):
        self.l = l
        self.m = m
        self.matrix = np.random.randint(1, 1000, size = (self.l, self.l))      
    def save_matrix(self):
        matrix_r = self.matrix
        np.savetxt('matrix.txt', matrix_r) # save the result of the original matrix
    def inner_product(self):   
        with open('matrix.txt', 'r') as f:
            original = np.loadtxt("matrix.txt", dtype='i', delimiter=' ')
        print("original matrix: \n", original)
        matrix = original
        for i in range(self.m - 1):
            matrix_l = np.random.randint(1, 1000, size = (self.l, self.l))          
            matrix = np.inner(matrix, matrix_l)
        np.savetxt('inner_product_matrix.txt', matrix) # save the result of the inner product matrix
    def read_file(self):
        with open('matrix.txt') as f:
            line = f.readline()    
            while line:
                print(line)
                line = f.readline()
        with open('inner_product_matrix.txt') as f:
            line = f.readline()    
            while line:
                print(line)
                line = f.readline()
            
matrix_result = matrix_calculation(5,2)
matrix_result.save_matrix()
matrix_result.inner_product()
matrix_result.read_file()











