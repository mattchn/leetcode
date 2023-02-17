class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def maxDepth(self, root):
   
   def depthFirstSearch(root, depth):
      if not root:
         return depth
      return max(depthFirstSearch(root.left, depth + 1), depthFirstSearch(root.right, depth + 1))
               
   return depthFirstSearch(root, 0)