def findKthPositive(arr, k):
   left, right = 0, 0
   count = 0
   while count < k and right < len(arr):
      if arr[right] - arr[left] - 1 >= k - count:
         return arr[left] + k - count
      count += arr[right] - arr[left] - 1
      left += 1
      right += 1
   return arr[right - 1] + k - count
