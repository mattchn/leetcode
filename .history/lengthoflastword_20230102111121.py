def lengthOfLastWord(s):
   if len(s) == 0:
      return 0
   elif s.rfind(" ") == -1:
      return len(s)
   else:
      last_space = s.rfind(" ")
      length = len(s[-1:last_space])
      return length
   