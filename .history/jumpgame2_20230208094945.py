def jump(nums):
   n = len(nums)
   jumps = [float('inf')] * n
   jumps[0] = 0
   
   for i in range(n):
      for j in range(i + 1, min(i + nums[i] + 1, n)):
         jumps[j] = min(jumps[j], jumps[i] + 1)
         
   return jumps[n - 1]