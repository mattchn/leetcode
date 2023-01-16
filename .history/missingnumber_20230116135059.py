def missingNumber(nums):
   highestNum = len(nums) + 1
   totalSum = 0
   while highestNum != 0:
      totalSum += highestNum
      highestNum -= 1
   numsSum = sum(nums)
   
   return (totalSum - numsSum)
   
      