def ifAnagram(word1, word2):
   if len(word1) != len(word2):
      return False

   anagram = 0
   
   for each_letter in word2:
      if each_letter in word1:
         anagram += 1
   
   return (len(word2) == anagram)

print(
ifAnagram('cccccccc', 'cattttttt')
)