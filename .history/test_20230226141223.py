import heapq

class TreeNode:
   def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def ifAnagram(word1, word2):
   if len(word1) != len(word2):
      return False

   return sorted(word1) == sorted(word2)

def firstAndLast(arr, target):
   def find_start(arr, target):
      if arr[0] == target:
         return 0
      
      left, right = 0, len(arr) -1
      
      while left <= right:
         mid = (left + right) // 2
         if arr[mid] == target and arr[mid - 1] < target:
            return mid
         elif arr[mid] < target:
            left = mid + 1
         else:
            right = mid - 1
      
      return -1
   
   def find_end(arr, target):
      if arr[-1] == target:
         return len(arr) - 1
      
      left, right = 0, len(arr) - 1
      
      while left <= right:
         mid = (left + right) // 2
         if arr[mid] == target and arr[mid + 1] > target:
            return mid
         elif arr[mid] > target:
            right = mid - 1
         else:
            left = mid + 1
      
      return -1
   
   first = find_start(arr, target)
   last = find_end(arr, target)
   
   return [first, last]
   
def kthLargest(arr, k):
   arr = [-elem for elem in arr]
   heapq.heapify(arr)
   for i in range(k-1):
      heapq.heappop(arr)
   
   return -heapq.heappop(arr)
   
def symmetricTree(root):
   root1 = root.left
   root2 = root.right
   
   def areSymmetric(root1, root2):
      if not root1 and not root2:
         return True
      elif(root1 is None != root2 is None) or root1.val != root2.val:
         return False
      else:
         return areSymmetric(root1.left, root2.right) and areSymmetric(root1.right, root2.left)
      
   if not root:
      return True
   
   return areSymmetric(root1, root2)
      
def generateParenthases(n):
   def rec(n, diff, comb, combs):
      if diff < 0 or diff > n:
         return
      elif n == 0:
         if diff == 0:
            combs.append(''.join(comb))
      else:
         comb.append('(')
         rec(n-1, diff+1, comb, combs)
         comb.pop()
         comb.append(')')
         rec(n-1, diff-1, comb, combs)
         comb.pop()   
   
   combs = []
   rec(2*n, 0, [], combs)
   return combs

def fibinacci(n):
   if n == 1 or n == 2:
      return 1
   
   bottom_up = [0 for i in range(n)]
   bottom_up[0] =  1
   bottom_up[1] =  1
   
   for i in range(n):
      bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
      print(bottom_up)
   
   return bottom_up[n - 1]
   


print(
fibinacci(3)
)