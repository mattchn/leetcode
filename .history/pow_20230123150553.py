def myPow(x, n):
   i = 0
   new_x = x
   
   if n < 0:
      new_x = new_x/10
   
   if n == 0:
      return 1
   
   while i < 0:
      new_x = new_x * x
      i += 1
      
   return new_x

print(myPow(2.0000,10))
print(2.0000 * 2.0000)