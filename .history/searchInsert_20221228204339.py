def searchInsert(nums, target):
   if nums.index(target):
      return nums.index(target)
   else:
      while target not in nums:
         target += 1
      return nums.index(target)


a = [1,2,3]   
print(a.index(2))