def ifAnagram(word1, word2):
   if len(word1) != len(word2):
      return False

   for each_letter in word2:
      if each_letter in word1:
         