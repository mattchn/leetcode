def findKthPositive(arr, k):
   n = len(arr)
   counter = 1
   i = 0
   
   while i < n and k > 0:
      if arr[i] == counter:
         i += 1
      else:
         k -= 1
         if k == 0:
               return counter
      counter += 1
      
   return arr[-1] + k
