def findDifference(nums1, nums2):    
   i = 0
   for each_num in nums1:
      if each_num in nums2:
            nums1.pop(i)
            nums2.pop(i)
      i += 1
   
   return [nums1, nums2]