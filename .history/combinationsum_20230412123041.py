def combinationSum(candidates, target):
   sums = []
   
   if min(candidates) > target:
      return sums
   
   def backtrack(candidates, target, path, sums):
      if target == 0:
         sums.append(path)
         return
      
      if target < 0:
         return
      
      for i in range(len(candidates)):
         if candidates[i] > target:
            break
         if i > 0 and candidates[i] == candidates[i - 1]:
            continue
         
         backtrack(candidates[i:], target - candidates[i], path + candidates[i])