class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def longestZigZag(root):
   tracker = 0
   
   if root.left:
      tracker += 1
      if root.left.right:
         tracker += 1
   
   