class ListNode:
   def __init__(self, val=0, next=None):
      self.val = val
      self.next = next
   
def reverseList(head):
   prev = None
   curr = head
   while curr:
      temp = curr.next 
      curr.next = prev
      prev = curr
      curr = temp
   
   return prev