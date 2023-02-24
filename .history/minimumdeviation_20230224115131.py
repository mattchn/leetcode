import heapq

def minimumDeviation(nums):
   #multiply all odd numbers by 2
   nums = [x * 2 if x % 2 == 1 else x for x in nums]
   min_val = min(nums)
   
   #make into max heap instead of min heap
   nums = [-x for x in nums]
   heapq.heapify(nums)
   diff = float('inf')
   
   while True:
      max_val = -heapq.heappop(nums)
      diff = min(diff, max_val - min_val)
      #if max val is odd number break because can't divide
      if max_val % 2 == 1:
         break
      #if not odd then divid max val by 2 and see if there is a new min val and then calculate difference again
      heapq.heappush(nums, -max_val // 2)
      min_val = min(min_val, max_val // 2)

   return diff
      
   
   