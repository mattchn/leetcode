def countOdds(low, high):
   if (low % 2 == 0) or (high % 2 == 1):
      return (high - low)//2 + 1
   else:
      return (high - low)//2

print(countOdds(8,10))