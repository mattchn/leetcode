def myPow(x, n):
   if n == 0:
      return 1
   if n < 0:
      x = 1 / x
      n = -n
   result = 1
   current_product = x
   i = n
   while i > 0:
      if i % 2 == 1:
         result *= current_product
      current_product *= current_product
      i //= 2
   return result


print(myPow(2, -2))