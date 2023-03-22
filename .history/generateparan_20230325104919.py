def generateParanthesis(n):
   
   #use backtracking
   def backtrack(result, curr, left, right):
      
      # we have n pairs already
      if left == right == n:
         result.append(curr)
         return
      
      if left < n:
         backtrack(result, curr + '(', left + 1, right)
      
      if right < left:
         backtrack(result, curr + ')', left, right + 1)
   
   result = []
   backtrack(result, '', 0, 0)
   
   return result