def searchInsert(nums, target):
   left = 0
   right = len(nums) - 1
   while left <= right:
      mid = (left + right) // 2
      if nums[mid] == target:
         return mid
      elif nums[mid] < target:
         left = mid + 1
      else:
         right = mid - 1
   return left

nums = [1,3,5,6]
num1 = [1,3]
print(searchInsert(nums, 5))
print(searchInsert(nums, 2))
print(searchInsert(num1, 1))