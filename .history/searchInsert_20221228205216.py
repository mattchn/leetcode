def searchInsert(nums, target):
   if target not in nums:
      nums.append(target)
      nums.sort()
      result = nums.index(target)
      return result
   else:
      result = int(nums.index(target))
      return result

nums = [1,3,5,6]
num1 = [1,3]

print(searchInsert(nums, 5))
print(searchInsert(nums, 2))
print(searchInsert(num1, 1))