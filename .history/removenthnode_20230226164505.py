class ListNode:
   def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

def removeNthFromEnd(head, n):
   dummy = ListNode(0)
   dummy.next = head
   slow = fast = dummy
   for i in range(n):
      fast = fast.next
   while fast.next:
      slow = slow.next
      fast = fast.next
   slow.next = slow.next.next
   return dummy.next