def isValid(self, s):
   mapping = {')':'(', ']':'[', '}':'{'}
   stack = []
   for char in s:
      if char in mapping:
            if not stack or stack.pop() != mapping[char]:
               return False
      else:
            stack.append(char)
   return not stack
