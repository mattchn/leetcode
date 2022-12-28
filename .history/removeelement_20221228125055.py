def removeElement(nums, val):
   if not nums:
      return 0
   
   pointer = 0
   for i in range(len(nums)):
      if nums[i] != val:
         nums[pointer] = nums[i]
         pointer += 1
         
   return pointer