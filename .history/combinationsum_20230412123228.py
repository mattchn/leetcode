def combinationSum(candidates, target):
   sums = []
   
   if min(candidates) > target:
      return sums
   
   def backtrack(candidates, target, path, sums):
      # if we find a valid combination
      if target == 0:
         sums.append(path)
         return
      
      # exceeded the target
      if target < 0:
         return
      
      # loop over candidate array and adding each element to the path 
      for i in range(len(candidates)):
         if candidates[i] > target:
            break
         if i > 0 and candidates[i] == candidates[i - 1]:
            continue
         
         backtrack(candidates[i:], target - candidates[i], path + [candidates[i]], sums)
   
   backtrack(candidates, target, [], sums)
   return sums