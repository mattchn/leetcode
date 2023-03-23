def rotate(matrix):
   n = len(matrix)
   
   # rotate each layer from outermost to innermost
   
   for layer in range(n // 2):
      first, last = layer, n - layer - 1
      
      # rotate each element in the layer
      for i in range(first, last):
         offset = i - first
         
         #save top left element
         temp = matrix[first][i]
         
         # top-left = bottom-left
         matrix[first][i] = matrix[last-offset][first]
         
         # bottom-left = bottom-right
         matrix[last-offset][first] = matrix[last][last-offset]
         
         # bottom-right = top-right
         matrix[last][last-offset] = matrix[i][last]
         
         # top-right = top-left
         matrix[i][last] = temp