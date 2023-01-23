def findJudge(n, trust):
   i = 0
   count = 0
   while i < n:
      if (trust[i][1] == trust[i + 1][1]):
         count += 1
         judge = trust[i][1]
         i += 1
      else:
         i += 1

   if (n - count == 1):
      return judge
   else:
      return -1