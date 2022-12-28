def removeDuplicates(nums):
   if not nums:
      return 0
   unique_nums = 1
   
   for i in range(1,len(nums)):
      if nums[i] != nums[i-1]:
         nums[unique_nums] = nums[i]
         unique_nums += 1
   
   return unique_nums


nums = [1,2,3,4,5]
print(nums.remove())

