def countOdds(low, high):
   count = 0
   counter = low
   if low == high:
      if (low % 2 != 0):
         return 1
      else:
         return count
   while counter <= high:
      if (counter % 2 == 0):
         counter += 1
      else:
         count += 1
         counter += 2
   return count

print(countOdds(8,10))