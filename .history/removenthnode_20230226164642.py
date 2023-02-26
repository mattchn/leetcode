class ListNode:
   def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

def removeNthFromEnd(head, n):
   dummy = ListNode(0)
   dummy.next = head
   
   #initialize two pointers and move the fast pointer n nodes ahead of slow
   slow = fast = dummy
   for i in range(n):
      fast = fast.next
      
   #use slow pointer to skip over node
   while fast.next:
      slow = slow.next
      fast = fast.next
   slow.next = slow.next.next
   return dummy.next