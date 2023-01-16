def containsNearbyDuplicate(nums, k):
   if len(nums) != len(set(nums)):
      return False
   else:
      