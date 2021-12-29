# return the maximum sum possible in the upper left quadrant of the matrix from flipping the matrix

def flippingMatrix(matrix):
    maxSum = 0
    n = len(matrix) # num of rows and columns n x n
    
    # Loop through the length of each quadrant
    for i in range(n//2):
        for j in range(n//2):
            maxSum += max(matrix[i][j], matrix[i][n - 1 - j], matrix[n - 1 - i][j], matrix[n - 1 - i][n - 1 - j])
            
    
    return maxSum
'''
# comparing the four corners
# n - 1 - j or -i- j is the code for finding "mirrored" elements in a matrix 
# n = 4
# 0,0 / [i][j]
# 0,3 / 0,-1 [i][n - 1 - j]
# 3,0 / -1,0 [n - 1 - i][j]
# 3,3 / -1, -1 [n - 1 - i][n - 1 - j]
            
            
[[112, 42, 83, 119],
[56, 125, 56, 49],
[15, 78, 101, 43],
[62, 98, 114, 108]]

# 112,119,62,108 which is the greatest element?

'''
