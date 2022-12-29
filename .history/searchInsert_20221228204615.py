def searchInsert(nums, target):
   if target not in nums:
      target += 1
      searchInsert(nums, target)
   else:
      return nums.index(target)
      


nums = [1,3,5,6]
print(searchInsert(nums, 2))