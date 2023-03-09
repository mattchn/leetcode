def moveZeroes(nums):
   for each_num in range(0, len(nums)):
      if each_num == 0:
         nums.pop(each_num)
         nums.append(each_num)
   
   return nums