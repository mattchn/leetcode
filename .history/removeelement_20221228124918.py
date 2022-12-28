def removeElement(nums, val):
   for i in range(1, len(nums)):
      if nums[i] != val:
         i += 1
      else:
         nums.remove(nums[i])
         i += 1
   return nums