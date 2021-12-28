# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

def diagonalDifference(arr):
  #O(n**2) Time Complexity
    sum1 = 0
    sum2 =  0
    for i in range(n): # i is the row number
        for j in range(n): # j is the number in the row
            if i == j:
                sum1 += arr[i][j] # sum of first diagonal;
                
            if i == (n - 1) - j: # if the row # is 2 - index needed
                sum2 += arr[i][j]
    
    return abs(sum1 - sum2)
  
 
def diagonalDifference2(arr):
  #O(n) Time Complexity
  leftdiag = rightdiag = 0
  for i in range(n):
    leftdiag += arr[i][i]
    rightdiag += arr[i][n-1-i]
    
   return abs(leftdiag-rightdiag)
      
