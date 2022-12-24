def mergeTwoLists(list1, list2):
   i = 0
   while list1.next != None:
      if list1.val(i) < list2.val(i):
         if list1.val(i+1) > list2.val(i):
            list1.next = list2
            i += 1
         else:
            list1.next = list1.next
            i += 1
      return list1