def searchInsert(nums, target):
   if nums.index(target):
      return nums.index(target)
   else:
      while target not in nums:
            target += 1
      return nums.index(target)

nums = [1,3,5,6]
print(searchInsert(nums, 2))