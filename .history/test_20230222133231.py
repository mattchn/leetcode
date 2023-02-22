def ifAnagram(word1, word2):
   if len(word1) != len(word2):
      return False

   freq1 = {}
   freq2 = {}
   
   for each_char in word1:
      if each_char in freq1:
         freq1[each_char] += 1
      else:
         freq1[each_char] = 1
         
   for each_char in word2:
      if each_char in freq2:
         freq2[each_char] += 1
      else:
         freq2[each_char] = 1
   
   for key in freq1:
      if key not in freq2 or freq1[key] != freq2[key]:
         return False
      else:
         return True
   

print(
ifAnagram('', '') 
)