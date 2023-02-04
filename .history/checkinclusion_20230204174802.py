def checkInclusion(s1, s2):
   if len(s1) > len(s2):
      return False
   
   s1_count = [0] * 26
   s2_count = [0] * 26
   
   for char in s1:
      s1_count[ord(char) - ord('a')] += 1

   for i in range(len(s2)):
      s2_count[ord(s2[i]) - ord('a')] += 1
      
      if i >= len(s1):
         s2_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
         
      if s1_count == s2_count:
         return True
      
   return False