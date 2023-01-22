class ListNode(object):
   def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

def addTwoNumbers(self,l1,l2):
   dummy = ListNode()
   current = dummy
   carry = 0
   while l1 or l2:
      x = l1.val if l1 else 0
      y = l2.val if l2 else 0
      s = carry + x + y
      carry = s // 10
      current.next = ListNode(s % 10)
      current = current.next
      if l1:
         l1 = l1.next
      if l2:
         l2 = l2.next
   if carry > 0:
      current.next = ListNode(carry)
   return dummy.next