def findDifference(nums1, nums2):    
   set1 = set(nums1)
   set2 = set(nums2)
   distinct_nums1 = set1.difference(set2)
   distinct_nums2 = set2.difference(set1)
   return [list(distinct_nums1), list(distinct_nums2)]