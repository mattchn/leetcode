def ifAnagram(word1, word2):
   if len(word1) != len(word2):
      return False

   return sorted(word1) == sorted(word2)

def firstAndLast(arr, target):
   result = [-1, -1]
   for i in range(len(arr)):
      if arr[i] == target:
         start = i
         
         while i + 1 < len(arr) and arr[i + 1] == target:
            i += 1
            
         return [start, i]

   return result
            
            
   

print(
firstAndLast([1,2,3,4,3], 5)
)