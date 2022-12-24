def longestCommonPrefix(strs):
   """
   :type strs: List[str]
   :rtype: str
   """
   if not strs:
      return ""
   if len(strs) == 1: 
      return strs[0]
   prefix = strs[0]
   for i in range(1, len(strs)):
      while strs[i].find(prefix) != 0:
         prefix = prefix[:-1]
         if not prefix:
               return ""
   return prefix

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["dog","dog","dog"]))