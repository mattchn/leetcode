def maxIceCream(costs, coins):
   sorted_icecream = sorted(costs)
   bars = 0
   i = 0
   while coins <= 0 or i <= len(costs):
      bars += 1
      coins = coins - sorted_icecream[i]
      i += 1
   return bars


coins = 7
costs = [1,1,2,3,4]
coins = coins - costs[0]
print(sorted([1,3,2,4,1]))
