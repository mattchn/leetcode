def isIsomorphic(s, t):
   mapping = {}
   
   for i in range(len(s)):
      if s[i] not in mapping:
         if t[i] in mapping.values():
            return False
         mapping[s[i]] = t[i]
      else:
         if mapping[s[i]] != t[i]:
            return False

   return True