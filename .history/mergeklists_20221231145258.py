

def mergeKLists(lists: List[ListNode]) -> ListNode:
   result = ListNode(0)
   curr = result
   heap = []
   for node in lists:
      if node:
         heap.append(node)
   heapq.heapify(heap)
   while heap:
      curr.next = heapq.heappop(heap)
      curr = curr.next
      if curr.next:
         heapq.heappush(heap, curr.next)
   return result.next