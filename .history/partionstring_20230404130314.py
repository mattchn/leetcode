def partionString(s):
   
   unique_ways = 0
   unique_letters = set(s)
   
   # if string is all unique return 1
   if len(unique_letters) == len(s):
      return 1
   
   while len(s) != 0:
      for each_letter in unique_letters:
         s -= each_letter
         unique_letters[each_letter].pop()
         unique_ways += 1
   
   return unique_ways


s = 'aaaab'
unique = set(s)

for each_letter in unique:
   print(each_letter)   

print(s - 'a')
