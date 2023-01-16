def missingNumber(nums):
   highestNum = len(nums) + 1
   totalSum = 0
   while highestNum != 0:
      totalSum += highestNum
      highestNum -= 1
   
   
      