def reverse(x):
   if x == 0:
      return x
   elif x > 2147483647 or x < -2147483648:
      return 0
   elif x < 0:
      new_x = int(x / -1)
      string_reverse = str(new_x)[::-1]
      int_reverse = int(string_reverse)
      result = -1 * int_reverse
      return result
   else:
      string_reverse = str(x)[::-1]
      return int(string_reverse)


print(int(-123/-1))
print(reverse(123))
print(reverse(-123))