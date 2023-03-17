def isAnagram(s, t):
   s_count = {}
   
   for each_char in s:
      if s_count[each_char]:
         s_count[each_char] += 1
      else:
         s_count[each_char] = 1
   
   