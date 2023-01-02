def lengthOfLastWord(s):
   if len(s) == 0:
      return 0
   elif s.rfind(" ") == -1:
      return len(s)
   else:
      last_space = s.rfind(" ")
      word = s[last_space + 1:-1]
      if word.isalpha():
         return len(word)
      else:
         
      
      return length
