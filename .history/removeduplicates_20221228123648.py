def removeDuplicates(nums):
   nums.sort()
   for i in range (len(nums)):
      if nums[i] == nums[i+1]:
         nums.pop(nums[i])
      return nums
   
print(removeDuplicates([1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]))