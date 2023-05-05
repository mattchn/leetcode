def maxVowels(s, k):
   max_vowel = 0
   vowels = ['a', 'e', 'i', 'o', 'u']
   for i in range(0, len(s) - k):
      for each_letter in s[i:i+k]:
         current_max = 0
         if each_letter in vowels:
            current_max += 1
         max_vowel = max(max_vowel, current_max)
      