def searchRange(nums, target):
   range = ['num1','num2']
   i = 0
   j = -1
   while nums[i] != nums[j]:
      if nums[i] == target:
         range[0] = nums[i]
         i += 1
      if nums[j] == target:
         range[1] = nums[j]
         j -= 1
      else:
         i += 1
         j -= 1
   
   if range == ['num1','num2']:
      return [-1,-1]
   else:
      return range