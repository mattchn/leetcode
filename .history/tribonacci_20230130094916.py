def tribonacci(n):
   if n == 0:
      return 0
   elif n == 1 or n == 2:
      return 1
   else:
      t = [0, 1, 1]
      for i in range (3, n + 1):
         t.append(t[i - 1] + t[i - 2] + t[i - 3])
      return t[n]