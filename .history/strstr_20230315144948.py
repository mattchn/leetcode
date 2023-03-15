def strStr(haystack, needle):
   count = 0
   length = len(needle)
   for each_char in haystack:
      if each_char == needle[0]:
         if haystack[count:count + length] == needle:
            return count
      else:
         count += 1
   
   return -1      
   