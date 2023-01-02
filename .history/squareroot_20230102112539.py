def mySqrt(x):
   left = 0
   right = x

   while left <= right:
      mid = (left + right) // 2
      mid_square = mid * mid

      if mid_square == x:
         return mid
      elif mid_square > x:
         right = mid
         left += 1
      else:
         left = mid
         right -= 1
   return left