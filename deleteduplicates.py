class ListNode(object):
   def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

def deleteDuplicates(head):
   if not head:
      return head
   curr = head
   while curr.next:
      if curr.val == curr.next.val:
         curr.next = curr.next.next
      else:
         curr = curr.next
   return head