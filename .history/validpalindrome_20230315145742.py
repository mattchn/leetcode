def isPalindrome(s):
   new_string = ''
   for each_char in s:
      if each_char.isalpha():
         new_string += each_char
   
   lower_string = new_string.lower()
   
   left, right = 0, -1
   while left < len(lower_string)//2:
      if lower_string[left] == lower_string[right]:
         