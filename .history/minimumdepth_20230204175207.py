class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def minDepth(root):
   if not root:
      return 0
   
   if not root.left:
      return minDepth(root.right) + 1
   
   if not root.right:
      return minDepth(root.left) + 1
   
   return min(minDepth(root.left), minDepth(root.right)) + 1
   