def minimumDeviation(nums):
   largest_num = max(nums)
   smallest_num = min(nums)
   difference = largest_num - smallest_num
   
   for each_num in nums:
      if (each_num > smallest_num) and (each_num // 2 == 0):
         each_num /= 2
      elif (each_num < largest_num) and (each_num // 2 != 0):
         each_num *= 2
   
   