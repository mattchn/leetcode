def isPowerOfThree(n):
   while n > 1:
      n /= 3
      if n % 3 == 0:
         n -= 3
      else:
         return False
   
   return True