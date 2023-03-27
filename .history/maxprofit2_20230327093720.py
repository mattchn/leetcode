def maxProfit(prices):
   n = len(prices)
   profit = 0
   
   for i in range(1, n):
      if prices[i] - prices[i - 1] > 0:
         difference = prices[i] - prices[i - 1]
         profit += difference
         
   return profit
