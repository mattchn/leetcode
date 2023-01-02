def detectCaptialUse(word):
   if word == word.upper():
      return True
   elif word[0] == word[0].upper() and word[1:] == word[1:].lower():
      return True
   elif word == word.lower():
      return True
   else:
      return False
