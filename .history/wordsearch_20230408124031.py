def exist(board, word):
   m = len(board)
   n = len(board[0])
   visited = [[False for j in range(n)] for i in range(m)]

   def dfs(i, j, k):
      if k == len(word):
         return True

      if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or board[i][j] != word[k]:
         return False

      visited[i][j] = True
      if dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or dfs(i, j+1, k+1) or dfs(i, j-1, k+1):
         return True

      visited[i][j] = False
      return False

   for i in range(m):
      for j in range(n):
         if board[i][j] == word[0]:
               if dfs(i, j, 0):
                  return True

   return False