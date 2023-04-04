def partionString(s):
   # if string is all unique return 1
   if sum(set(s)) == s:
      return 1

s = 'aaab'
c = sum(set(s))

print(c)