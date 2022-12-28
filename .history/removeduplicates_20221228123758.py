def removeDuplicates(nums):
   nums.sort()
   i = 1
   while i < len(nums):
      if nums[i] == nums[i-1]:
         nums.pop(i)
         i += 1
      else:
         i += 1
      return nums
   
print(removeDuplicates([1,101,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]))