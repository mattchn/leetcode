def arraySign(nums):
   product = 1
   for each_num in nums:
      if each_num < 0:
            product *= -1
      elif each_num > 0:
            product *= 1                
      else:
            return 0
   
   return product