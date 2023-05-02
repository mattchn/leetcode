def arraySign(nums):
   product = 1
   for each_num in nums:
      product *= each_num
   
   if product > 0:
      return 1
   elif product == 0:
      return 0
   else:
      return -1