def permute(nums):
   if len(nums) <= 0:
      return [nums]
   result = []
   for i in range(len(nums)):
      for perm in permute(nums[:i] + nums[i + 1:]):
         result.append([nums[i] + perm])
   
   return result
   