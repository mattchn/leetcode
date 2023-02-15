def addToArrayForm(num, k):
   n = 0
   for i in range(len(num)):
      n += num[i] * 10**(len(num)-i-1)
   s = n + k
   return [int(digit) for digit in str(s)]
   