from collections import deque 

class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def deepestLeavesSum(root):
   q = deque([(root, 0)])
   max_depth = -1
   sum_of_deepest = 0
   
   while q:
      node, depth = q.popleft()
      if not node.left and not node.right:
         if depth == max_depth:
            sum_of_deepest += node.val
         elif depth > max_depth:
            max_depth = depth
            sum_of_deepest = node.val
      
      if node.left:
         q.append((node.left, depth + 1))
      if node.right:
         q.append((node.right, depth + 1))
   
   return sum_of_deepest