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


nums = [1,101,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
print(nums.remove(1))
print(removeDuplicates([1,101,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]))