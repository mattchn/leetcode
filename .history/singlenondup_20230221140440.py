def singleNonDuplicate(nums):
   left, right = 0, len(nums) - 1
   while left < right:
      mid = (left + right) // 2
      if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
         return nums[mid]
      elif mid % 2 == 0 and nums[mid] == nums[mid + 1] or mid % 2 == 1 and nums[mid] == nums[mid - 1]:
         left = mid + 1
      else:
         right = mid - 1
   return nums[left]