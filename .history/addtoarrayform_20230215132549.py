def addToArrayForm(num, k):
   result = []
   carry = 0
   i = len(num) - 1
   while i >= 0 or k > 0 or carry > 0:
      digit = carry
      if i >= 0:
         digit += num[i]
      if k > 0:
         digit += k % 10
         k //= 10
      carry, digit = divmod(digit, 10)
      result.append(digit)
      i -= 1
   return result[::-1]               
   
   