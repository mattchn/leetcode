def searchRange(nums, target):
   def binary_search_left(nums, target):
      left, right = 0, len(nums) - 1
      while left <= right:
         mid = (left + right) // 2
         if nums[mid] >= target:
               right = mid - 1
         else:
               left = mid + 1
      return left
   def binary_search_right(nums, target):
      left, right = 0, len(nums) - 1
      while left <= right:
         mid = (left + right) // 2
         if nums[mid] <= target:
               left = mid + 1
         else:
               right = mid - 1
      return right
   
   left_index = binary_search_left(nums, target)
   right_index = binary_search_right(nums, target)
   if left_index <= right_index:
      return [left_index, right_index]
   else:
      return [-1, -1]