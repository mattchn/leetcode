def searchInsert(nums, target):
   if target not in nums:
      nums.append(target)
      nums.sort()
      return nums.index(target)
   if nums.index(target):
      result = int(nums.index(target))
      return result

nums = [1,3,5,6]
num1 = [1,3]

print(searchInsert(nums, 5))
print(searchInsert(nums, 2))
print(num1.index(1))