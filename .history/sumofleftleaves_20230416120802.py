class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right


def sumOfLeftLeaves(root):
   dummy = TreeNode()
   dummy = root
   
   sum = 0
   
   sum += dummy.left
   while dummy.left and dummy.right:
      sum += sumOfLeftLeaves(dummy.left)
      sum += sumOfLeftLeaves(dummy.right)
   
   return sum