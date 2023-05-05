def maxVowels(s, k):
   vowels = set(['a', 'e', 'i', 'o', 'u'])
   max_count = 0
   count = 0
   for i in range(len(s)):
      if i >= k and s[i-k] in vowels:
         count -= 1
      if s[i] in vowels:
         count += 1
      max_count = max(max_count, count)
   return max_count
      