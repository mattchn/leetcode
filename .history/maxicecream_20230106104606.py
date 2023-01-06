def maxIceCream(costs, coins):
   sorted_icecream = sorted(costs)
   bars = 0
   i = 0
   while coins <= 0 or i <= len(costs):
      bars += 1
      coins = coins - sorted_icecream[i]
      i += 1
   return bars

print(sorted([1,3,2,4,1]))
print(maxIceCream([1,3,2,4,1],7))