def searchRange(nums, target):
   range = []
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
   
   if range == []:
      return [-1,-1]
   else:
      return range