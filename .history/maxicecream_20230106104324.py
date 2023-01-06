def maxIceCream(cost, coins):
   sorted_icecream = cost.sort()
   bars = 0
   i = 0
   while coins <= 0 or i <= len(cost):
      bars += 1
      coins = coins - cost[i]
      i += 1
   return bars