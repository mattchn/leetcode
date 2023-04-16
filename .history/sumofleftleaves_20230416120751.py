class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right


def sumOfLeftLeaves(root):
   dummy = TreeNode()
   dummy = root
   
   sum = 0
   
   sum += root.left
   while root.left and root.right:
      sum += sumOfLeftLeaves(root.left)
      sum += sumOfLeftLeaves(root.right)
   
   return sum