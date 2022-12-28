def removeDuplicates(nums):
   nums.sort()
   i = 1
   while i < len(nums):
      if nums[i] == nums[i-1]:
         nums.remove(nums[i])
         i += 1
      else:
         i += 1
      return nums


nums = [1,2,3,4,5]
print(nums.remove(2))

