def strStr(haystack, needle):
   count = 0
   for each_char in haystack:
      if each_char == needle:
         return count
      else:
         count += 1
   
   return -1      
   