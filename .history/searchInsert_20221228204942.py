def searchInsert(nums, target):
   if target not in nums:
      nums.append(target)
      nums.sort()
      return nums.index(target)
   if len(nums) == 1:
      return nums.index(target)
   if nums.index(target):
      return nums.index(target)

nums = [1,3,5,6]
num1 = [1]

print(searchInsert(nums, 5))
print(searchInsert(nums, 2))
print(searchInsert(num1, 1))