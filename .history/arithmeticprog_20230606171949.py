def canMakeArithmeticProgression(self, arr):
   arr.sort()
   for i in range(1, len(arr)):
      number = arr[1] - arr[0]
      if arr[i] - arr[i - 1] != number:
            return False
      else:
            i += 1
   
   return True