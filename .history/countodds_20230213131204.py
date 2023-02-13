def countOdds(low, high):
   difference = high - low
   if (low == high):
      if (low % 2 == 0):
         return 0
      else:
         return 1
      
   if (difference % 2 == 0):
      return difference//2
   else:
      return difference//2 + 1

print(countOdds(8,10))