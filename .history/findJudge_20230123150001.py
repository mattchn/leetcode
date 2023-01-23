def findJudge(n, trust):
   i = 0
   count = 0
   
   if len(trust) == 1:
      if trust[0][1] == n:
         return n
      else:
         return -1
   
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