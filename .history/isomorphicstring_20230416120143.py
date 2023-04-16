def isIsomorphic(s, t):
   map = {}
   word = ''
   
   if len(s) != len(t):
      return False
   
   for each_index in range(0, len(s) - 1):
      if s[each_index] in map:
         word += map[s[each_index]]
      else:
         map[s[each_index]] = t[each_index]
         word += t[each_index]
   
   return word == t