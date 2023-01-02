def lengthOfLastWord(s):
   if len(s) == 0:
      return 0
   elif s.rfind(" ") == -1:
      return len(s)
   else:
      last_space = s.rfind(" ")
      length = len(s[last_space + 1:-1])
      return length
