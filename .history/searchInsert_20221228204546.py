def searchInsert(nums, target):
   if target in nums:
      if nums.index(target):
         return nums.index(target)
   else:
      target += 1
      searchInsert(nums, target)


nums = [1,3,5,6]
print(searchInsert(nums, 2))