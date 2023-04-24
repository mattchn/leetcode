def lastStoneWeight(stones):
   while len(stones) > 1:
      stones.sort()
      heaviest = stones[-1]
      second = stones[-2]
      result = heaviest - second
      if result != 0:
         stones.append(result)
      stones.pop(heaviest)
      stones.pop(second)
   
   return stones[0]