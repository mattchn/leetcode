def mergeTwoLists(list1, list2):
   for i in range (len(list2)):
      if list1.val(i) < list2.val(i):
         if list1.val(i+1) > list2.val(i):
            list1.next = list2
         else:
            list1.next = list1.next
      return list1