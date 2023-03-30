def intersect(nums1, nums2):
   intersect = []
   for i in range(0, len(nums1)):
      if nums1[0] in nums2:
         intersect.append(nums1[0])
         