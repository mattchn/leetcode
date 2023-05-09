def sprialOrder(matrix):
   if not matrix:
      return 0
   
   sprial_matrix = []
   m, n = len(matrix), len(matrix[0])
   top, bottom, left, right = 0, m -1, 0, n - 1
      
   while top <= bottom and left <= right:
      # traverse from lef tot right along the top row
      for j in range(left, right + 1):
         sprial_matrix.append(matrix[top][j])
      
      top += 1
      
      # traverse from top to bottom along the right row
      for i in range()