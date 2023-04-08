def exist(board, word):
   m = len(board)
   n = len(board[0])
   
   # initialize a boolean matrix for if we already have visted this index
   visited = [[False for j in range(n)] for i in range(m)]

   def dfs(i, j, k):
      # return true if find entire word
      if k == len(word):
         return True

      # check if current index matches current character in the word
      if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or board[i][j] != word[k]:
         return False

      # if the current character is in the current index
      visited[i][j] = True
      
      # find next character in adjacent indexes
      if dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1):
         return True

      # if you can't find it then it's false
      visited[i][j] = False
      return False

   for i in range(m):
      for j in range(n):
         if board[i][j] == word[0]:
               if dfs(i, j, 0):
                  return True

   return False