def containsDuplicate(nums):
   sortedNums = sorted(nums)
   result = True
   i = 1
   while i < len(sortedNums):
      if sortedNums[i] == sortedNums[i-1]:
         result = True
         i += 1
      else:
         result = False
         return result