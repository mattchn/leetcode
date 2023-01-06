def maxIceCream(costs, coins):
   sorted_icecream = costs.sort()
   bars = 0
   i = 0
   while coins <= 0 or i <= len(costs):
      bars += 1
      coins = coins - sorted_icecream[i]
      i += 1
   return bars