def partionString(s):
   # if string is all unique return 1
   if set(s) == s:
      return 1

s = 'aaab'
c = set(s)

print(c)