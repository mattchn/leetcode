def mincostTicket(days, costs):
   # use dynamic programming
   dp = [0] * 366
   for i in range(1, len(dp)):
      if i not in days:
         dp[i] = dp[i-1]
      else:
         dp[i] = min(dp[i-1] + costs[0], dp[max(0, i-7)] + costs[1], dp[max(0, i-30)] + costs[2])
   return dp[days[-1]]