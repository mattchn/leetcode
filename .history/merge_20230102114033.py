def merge(nums1, m , nums2, n):
   new_nums1 = nums1[:m]
   new_nums2 = nums2[:n]
   merge_list = new_nums1 + new_nums2
   
   return merge_list.sort()
   