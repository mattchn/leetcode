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
      
      # traverse from top to bottom along the right column
      for i in range(top, bottom + 1):
         sprial_matrix.append(matrix[i][right])
      right -= 1
      
      # traverse from right to left along bottom row if top is still above bottom
      if top <= bottom:
         for j in range(right, left - 1, -1):
               sprial_matrix.append(matrix[bottom][j])
         bottom -= 1

      # traverse from bottom to top along left column if left is still left of right
      if left <= right:
         for i in range(bottom, top - 1, -1):
               sprial_matrix.append(matrix[i][left])
         left += 1
   
   return sprial_matrix