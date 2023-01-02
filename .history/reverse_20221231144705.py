def reverse(x):
   if x < 0:
      x / -1
      string_reverse = str(x)[::-1]
      int_reverse = int(string_reverse)
      result = -1 * int_reverse
      return result
   else:
      string_reverse = str(x)[::-1]
      return int(string_reverse)


print(reverse(123))