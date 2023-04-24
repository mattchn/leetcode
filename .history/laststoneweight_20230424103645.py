def lastStoneWeight(stones):
   while len(stones) > 1:
      stones.sort()
      result = stones[-1] - stones[-2]
      if result != 0:
         stones.append(result)
      stones.pop(stones[-1])
      stones.pop(stones[-2])
   
   return stones[0]