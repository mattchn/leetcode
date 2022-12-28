def removeDuplicates(nums):
   nums.sort()
   for i in range (len(nums)):
      if nums[i] == nums[i+1]:
         nums.pop(nums[i])
      return nums.length