class ListNode:
   def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

def isPalindrome(head):
   if not head or not head.next:
      return True
   
   # find the middle of the list
   slow = head
   fast = head
   while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
   
   # reverse the second half of the list
   prev = None
   curr = slow
   while curr:
      temp = curr.next
      curr.next = prev
      prev = curr
      curr = temp
   
   # compare the first half with the reversed second half
   p1 = head
   p2 = prev
   while p2:
      if p1.val != p2.val:
         return False
      p1 = p1.next
      p2 = p2.next
   
   return True