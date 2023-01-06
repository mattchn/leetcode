def maxIceCream(costs, coins):
   sorted_icecream = sorted(costs)
   bars = 0
   i = 0
   while coins <= 0 or i <= len(costs):
      bars += 1
      coins -= sorted_icecream[i]
      i += 1
   return bars


coins = 7
costs = [1,1,2,3,4]
coins = coins - costs[0]
print(coins)
print(maxIceCream([1,3,4,2,1], 7))
