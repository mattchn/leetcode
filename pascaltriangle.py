def generate(numRows):
   triangle = []
   for row in range(numRows):
      new_row = [1] * (row + 1)
      for i in range(1, row):
         new_row[i] = triangle[row-1][i-1] + triangle[row-1][i]
      triangle.append(new_row)
   return triangle