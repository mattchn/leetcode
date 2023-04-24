def lastStoneWeight(stones):
   
   stones.sort(reverse=True)
   while len(stones) > 1:
      heaviest = stones.pop(0)
      second = stones.pop(0)
      
      if heaviest != second:
         stones.insert(0, heaviest - second)
         stones.sort(reverse=True)
   
   return stones[0] if len(stones) > 0 else 0