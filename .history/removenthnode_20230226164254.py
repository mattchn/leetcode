class ListNode:
   def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

def removeNthFromEnd(head, n):
   n_count = 0
   while n_count != n:
      head.next
      n_count += 1
   
   head.next = head.next.next
   
   return head