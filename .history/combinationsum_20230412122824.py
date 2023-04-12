def combinationSum(candidates, target):
   sums = []
   
   if min(candidates) > target:
      return sums
   
   