def isValid(s):
   pairs = {')':'(', ']':'[', '}':'{'}
   stack = []
   for c in s:
      if c in pairs:
         stack.append(c)
      elif not stack or pairs[c] != stack.pop():
         return False
   return not stack