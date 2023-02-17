class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def maxDepth(self, root):
   if not root:
      return 0
   
   left_depth = maxDepth(root.left)
   right_depth = maxDepth(root.right)
   
   return 1 + max(left_depth, right_depth)