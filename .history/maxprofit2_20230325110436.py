def maxProfit(prices):
   difference = []
   n = len(prices)
   
   for i in range(1, n - 1):
      difference.append(prices[i] - prices[i - 1])
   
   print(difference)
   return

prices = [7, 1, 5, 3, 6, 4]
maxProfit(prices)