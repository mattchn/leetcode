def dfs(node):
      nonlocal longest
      if not node:
         return (0, 0)
      
      left = dfs(node.left)
      right = dfs(node.right)
      
      longest = max(longest, left[1], right[0])
      return (left[1] + 1, right[0] + 1)
   
   longest = 0
   dfs(root)
   return longest