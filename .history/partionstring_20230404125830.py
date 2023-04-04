def partionString(s):
   # if string is all unique return 1
   if str(set(s)) == s:
      return 1

s = 'aaab'
c = str(set(s))

print(c)