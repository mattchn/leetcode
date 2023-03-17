def isAnagram(s, t):
   freq = {}
   
   if len(s) != len(t):
      return False
   
   for each_char in s:
      if each_char in freq:
         freq[each_char] += 1
      else:
         freq[each_char] = 1
   
   for each_char in t:
      if each_char in freq:
         freq[each_char] -= 1
         if freq[each_char] < 0:
            return False
      else:
         return False
   
   return True
   