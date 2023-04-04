def partionString(s):
   # if string is all unique return 1
   if len(set(s)) == len(s):
      return 1
   
   last_occurrence = {}
   start = 0
   result = []
   
   for i, c in enumerate(s):
      if c in last_occurrence:
         # Move the start of the substring to the next character after the last occurrence of c
         start = max(start, last_occurrence[c] + 1)
      
      last_occurrence[c] = i
      
      # If the current substring contains only unique characters, add it to the result
      if all(i > last_occurrence[char] for char in set(s[start:i+1])):
         result.append(s[start:i+1])
         start = i + 1
         
   return len(result)