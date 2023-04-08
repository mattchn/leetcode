def exist(board, word):
   i = 0
   result = ''
   
   for each_row in board:
      for each_letter in each_row:
         if word[i] == each_letter:
            result += each_letter
            i += 1