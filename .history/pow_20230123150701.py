def myPow(x, n):
   i = 0
   new_x = x
   
   if n < 0:
      new_x = new_x/10
   
   if n == 0:
      return 1
   
   while i < n - 1:
      new_x = new_x * x
      i += 1
      
   return new_x
