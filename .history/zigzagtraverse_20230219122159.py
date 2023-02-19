class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right
      
def zigzagLevelOrder(root):
   if not root:
      return []
   
   queue = [root]
   result = []
   level = 0
   
   while queue:
      level_size = len(queue)
      level_nodes = []
      
      for i in range(level_size):
         node = queue.pop(0)
         level_nodes.append(node.val)
         
         if node.left:
            queue.append(node.left)
         
         if node.right:
            queue.append(node.right)
      
      if level % 2 == 0:
         result.append(level_nodes)
      
      else:
         result.append(level_nodes[::-1])
      
      level += 1
   
   return result