def mergeAlternately(self, word1, word2):
   result = ""
   # Get the length of each word
   len1 = len(word1)
   len2 = len(word2)

   # Find the minimum length between the two words
   min_len = min(len1, len2)

   # Loop through the words up to the minimum length
   for i in range(min_len):
      # Add a letter from word1
      result += word1[i]
      # Add a letter from word2
      result += word2[i]
      
   result += word1[min_len:]
   result += word2[min_len:]

   return result