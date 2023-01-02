def reverse(x):
   if x < 0:
      int(x / -1)
      string_reverse = str(x)[::-1]
      int_reverse = int(string_reverse)
      result = -1 * int_reverse
      return result
   else:
      string_reverse = str(x)[::-1]
      return int(string_reverse)


print(-123/-1)
print(reverse(123))
print(reverse(-123))