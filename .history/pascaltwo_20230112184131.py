def getRow(rowIndex):
   row = [1]
   for i in range(1, rowIndex + 1):
      row.append(int(row[i-1] * (rowIndex - i + 1) / i))
   return row