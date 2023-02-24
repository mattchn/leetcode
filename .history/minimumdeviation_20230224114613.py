def minimumDeviation(nums):
   nums = [num * 2 if num % 2 == 1 else num for num in nums]
   nums.sort(reverse=True)
   min_deviation = float('inf')
      
   
   