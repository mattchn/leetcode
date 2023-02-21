def singleNonDuplicate(nums):
   left, right = 0, len(nums) - 1
   while left < right:
      mid = (left + right) // 2
      