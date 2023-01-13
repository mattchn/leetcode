def containsDuplicate(nums):
   sortedNums = sorted(nums)
   i = 1
   while i <= len(sortedNums):
      if sortedNums[i] == sortedNums[i-1]:
         return True
      else:
         return False