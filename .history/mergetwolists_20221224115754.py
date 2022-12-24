class ListNode:
   def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode):
   dummy = ListNode(0)
   current = dummy
   
   while list1 and list2:
      if list1.val < list2.val:
         current.next = list1
         list1 = list1.next
      else:
         current.next = list2
         list2 = list2.next
      current = current.next
      
   current.next = list1 or list2
   
   return dummy.next