class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def minDiffInBst(self, root):
   self.prev = None
   self.min_diff = float('inf')
   
   def inorder(node):
      if not node:
            return

      inorder(node.left)
      if self.prev:
            self.min_diff = min(self.min_diff, node.val - self.prev.val)
            
      self.prev = node
      inorder(node.right)
   
   inorder(root)
   
   return self.min_diff