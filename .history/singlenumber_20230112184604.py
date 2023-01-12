def singleNumber(nums):
   uniqueNums = []
   for eachNum in nums:
      if eachNum not in uniqueNums:
         uniqueNums.append(eachNum)
      else:
         uniqueNums.remove(eachNum)
   return uniqueNums[0]

