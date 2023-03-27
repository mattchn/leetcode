def maxProfit(prices):
   difference = []
   n = len(prices)
   profit = 0
   
   for i in range(1, n):
      difference.append(prices[i] - prices[i - 1])
   
   for each_profit in difference:
      if each_profit > 0:
         profit += each_profit
         
   return profit
