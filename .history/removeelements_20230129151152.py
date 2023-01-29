class ListNode:
   def __init__(self, val=0, next=None):
      self.val = val
      self.next = next
      
def removeElements(self, head, val):
   while head.next:
      if head.next.val = val:
         head.next = head.next.next
   return head