def numSubSeq(nums, target):
   array = []
   for i in range(len(nums) - 1):
      if nums[i] <= target//2:
         if nums[i] + nums[i] <= target:
            array.append(nums[i], nums[j])