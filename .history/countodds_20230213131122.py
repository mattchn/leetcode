def countOdds(low, high):
   difference = high - low
   if (low == high):
      if (low % 2 == 0):
         return 0
      else:
         return 1
   return difference//2

print(countOdds(8,10))