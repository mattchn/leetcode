s = "1234 12314 12313 "
last_space = s.rfind(" ")
while s[-1].isalpha() == False:
   s = s[:-2]
print(s)
print(s[last_space + 1:-1])