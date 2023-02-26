def longestPalindrome(s):
   n = len(s)
   #use dynamic programming where dp[i][j] is a boolean where true if s[i:j + 1] is a palindrome and false otherwise
   dp = [[False] * n for _ in range(n)]
   
   #all single characters are palindromes
   for i in range(n):
      dp[i][i] = True
      longest_palindrome = s[i]
   
   #palindrome if two characters are same
   for i in range(n - 1):
      if s[i] == s[i + 1]:
         dp[i][i + 1] = True
         longest_palindrome = s[i:i + 2]
   
   #for strings that are longer than 2 characters
   for length in range(3, n + 1):
      for i in range(n - length + 1):
         j = i + length - 1
         if s[i] == s[j] and dp[i + 1][j - 1]:
            dp[i][j] = True
            if length > len(longest_palindrome):
               longest_palindrome = s[i:j + 1]
   
   return longest_palindrome