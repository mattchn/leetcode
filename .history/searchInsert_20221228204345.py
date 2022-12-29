def searchInsert(nums, target):
   if nums.index(target):
      return nums.index(target)
   else:
      while target not in nums:
         target += 1
      return nums.index(target)


 
print(a.index(2))