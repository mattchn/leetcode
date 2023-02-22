def ifAnagram(word1, word2):
   if len(word1) != len(word2):
      return False

   return sorted(word1) == sorted(word2)

def firstAndLast(arr, target):
   first_index = 0
   last_index = -1
   result = [-1, -1]
   while first_index < len(arr) or (result[0] != -1 and result[1] != -1):
      if (arr[first_index] == target):
         result[0] = first_index
      else:
         first_index += 1
      
      if(arr[last_index] == target):
         result[1] = last_index
      else:
         last_index -= 1
   

print(
firstAndLast([1,2,3,4,3], 3)
)