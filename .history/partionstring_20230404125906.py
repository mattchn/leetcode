def partionString(s):
   # if string is all unique return 1
   if len(set(s)) == len(s):
      return 1

s = 'aaab'
c = len(set(s))

print(c)