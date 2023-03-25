def maxProfit(prices):
   difference = []
   n = len(prices)
   
   for i in range(1, n - 1):
      difference.append(prices[i] - prices[i - 1])
   
   print(difference)