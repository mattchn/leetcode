s = "1234 12314 12313 "
last_space = s.rfind(" ")
while s[-1].isspace() == True:
   s = s[:-2]
print(s)
