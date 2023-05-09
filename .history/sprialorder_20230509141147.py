def sprialOrder(matrix):
   if not matrix:
      return 0
   
   sprial_matrix = []
   m, n = len(matrix), len(matrix[0])
   top, bottom, left, right = 0, m -1, 0, n - 1
   
   # 