def findAnagrams(s, p):
   res = []
   n, m = len(s), len(p)
   if n < m:
      return res
   p_count = [0] * 26
   s_count = [0] * 26
   for i in range(m):
      p_count[ord(p[i]) - ord('a')] += 1
      s_count[ord(s[i]) - ord('a')] += 1
   for i in range(n - m):
      if p_count == s_count:
         res.append(i)
      s_count[ord(s[i]) - ord('a')] -= 1
      s_count[ord(s[i + m]) - ord('a')] += 1
   if p_count == s_count:
      res.append(n - m)
   return res