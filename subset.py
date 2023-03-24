def subset(nums):
   
   #use backtracking
   def backtrack(start, curr):
      result.append(curr)
      for i in range(start, n):
         backtrack(i + 1, curr + [nums[i]])
   
   n = len(nums)
   result = []
   backtrack(0, [])
   
   return result