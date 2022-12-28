def removeElement(nums, val):
   if not nums:
      return 0
   
   pointer = 0
   for i in range(len(nums)):
      if nums[i] != val:
         nums[pointer] = nums[i]
         pointer += 1
         
   return pointer

print(removeElement([3,2,2,3], 3))