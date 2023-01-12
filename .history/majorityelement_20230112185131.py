def majorityElement(nums):
   nums_dict = {}
   for num in nums:
      if num in nums_dict:
         nums_dict[num] += 1
      else:
         nums_dict[num] = 1
   return max(nums_dict, key=nums_dict.get)