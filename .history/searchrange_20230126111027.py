def searchRange(nums, target):
   range = ['num1','num2']
   i = 0
   j = -1
   while nums[i] != nums[j]:
      if nums[i] == target:
         range[0] = i
         i += 1
      if nums[j] == target:
         range[1] = j
         j -= 1
      else:
         i += 1
         j -= 1
   
   if range == ['num1','num2']:
      return [-1,-1]
   if range[0] == 'num1':
      return [range[1],range[1]]
   else: 
      return range