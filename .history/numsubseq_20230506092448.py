def numSubSeq(nums, target):
   array = []
   for i in range(len(nums) - 1):
      if nums[i] <= target//2:
         number = nums[i]
         while number <= target:
            for j in range(1, len(nums) - i):
               if number + nums[i + j] <= target:
                  array.append(number)
         else:
            array.append(number)