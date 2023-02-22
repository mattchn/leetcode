def ifAnagram(word1, word2):
   if len(word1) != len(word2):
      return False

   return sorted(word1) == sorted(word2)

def firstAndLast(arr, target):
   def find_start(arr, target):
      if arr[0] == target:
         return 0
      
      left, right = 0, len(arr) -1
      
      while left <= right:
         mid = (left + right) // 2
         if arr[mid] == target and arr[mid - 1] < target:
            return mid
         elif arr[mid] < target:
            left = mid + 1
         else:
            right = mid - 1
      
      return -1
   
   def find_end(arr, target):
      if arr[-1] == target:
         return len(arr) - 1
      
      left, right = 0, len(arr) - 1
      
      while left <= right:
         mid = (left + right) // 2
         if arr[mid] == target and arr[mid + 1] > target:
            return mid
         elif arr[mid] > target:
            right = mid - 1
         else:
            left = mid + 1
      
      return -1
   
   first = find_start(arr, target)
   last = find_end(arr, target)
   
   return [first, last]
   

print(
firstAndLast([1,2,3,3,3,3,3,3,4,5], 3)
)