def reverse(x):
   if x == 0:
      return 0

   result = 0
   if x < 0:
      new_x = int(x / -1)
      string_reverse = str(new_x)[::-1]
      int_reverse = int(string_reverse)
      result = -1 * int_reverse
      return result
   
   else:
      while x > 0:
         digit = x % 10
         if result > 214748364 or (result == 214748364 and digit > 7):
               return 0
         if result < -214748364 or (result == -214748364 and digit < -8):
               return 0
         result = result * 10 + digit
         x = x // 10

   return result


print(int(-123/-1))
print(reverse(123))
print(reverse(-123))

