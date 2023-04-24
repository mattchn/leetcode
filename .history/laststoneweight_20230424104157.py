def lastStoneWeight(stones):
   
   if len(stones) == 2:
      return stones[1] - stones[0]
   
   while len(stones) > 3:
      stones.sort()
      heaviest = stones[-1]
      second = stones[-2]
      result = heaviest - second
      if result != 0:
         stones.append(result)
      stones.pop()
      stones.pop()
   
   return stones[1] - stones[0]