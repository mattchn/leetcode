def diagonalSum(mat):
   num_of_rows = len(mat)
   sum = 0
   i = 0 
   while i in range(num_of_rows):
      if mat[i] != mat[0] or mat[-1]:
         if mat[i][i] == mat[i][-i]:
            sum += mat[i][i]
         else:
            sum += mat[i][i]
            sum += mat[i][-i]
      else:
         sum += mat[i][0]
         sum += mat[i][-1]
