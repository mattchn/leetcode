def diagonalSum(mat):
   n = len(mat)
   sum = 0
   for i in range(n):
      sum += mat[i][i] # add primary diagonal element
      if i != n - i - 1: # exclude elements in primary diagonal
         sum += mat[i][n - i - 1] # add secondary diagonal element
   return sum
