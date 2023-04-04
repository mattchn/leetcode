def partionString(s):
   
   seen_chars = set()
   count = 0
   
   # if string is all unique return 1
   if len(seen_chars) == len(s):
      return 1
   
   for i, char in enumerate(s):
      if char in seen_chars:
            count += 1
            seen_chars.clear()
      seen_chars.add(char)
      
   return count + 1