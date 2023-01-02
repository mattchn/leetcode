def lengthOfLongestSubstring(s):
   max_length = 0
   start = 0
   char_index = {}

   for i in range(len(s)):
      if s[i] in char_index:
         start = max(start, char_index[s[i]] + 1)
      char_index[s[i]] = i
      max_length = max(max_length, i - start + 1)

   return max_length
   