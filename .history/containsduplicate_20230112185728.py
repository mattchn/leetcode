def containsDuplicate(nums):
   sortedNums = sorted(nums)
   result = False
   i = 1
   while i < len(sortedNums):
      if sortedNums[i] == sortedNums[i-1]:
         result = False
         i += 1
      else:
         result = True
         return result