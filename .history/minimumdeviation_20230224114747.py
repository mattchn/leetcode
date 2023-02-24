import heapq

def minimumDeviation(nums):
   nums = [x * 2 if x % 2 == 1 else x for x in nums]
   min_val = min(nums)
   nums = [-x for x in nums]
   heapq.heapify(nums)
   diff = float('inf')
   while True:
      max_val = -heapq.heappop(nums)
      diff = min(diff, max_val - min_val)
      if max_val % 2 == 1:
         break
      heapq.heappush(nums, -max_val // 2)
      min_val = min(min_val, max_val // 2)
   return diff
      
   
   