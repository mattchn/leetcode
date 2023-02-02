class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def inorderTraversal(root):
   res = []
   stack = []
   while root or stack:
      while root:
         stack.append(root)
         root = root.left
      root = stack.pop()
      res.append(root.val)
      root = root.right
   return res