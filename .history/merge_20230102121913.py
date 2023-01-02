def merge(nums1, m , nums2, n):
   p1 = 0
   p2 = 0
   while p1 < m and p2 < n:
      if nums1[p1] <= nums2[p2]:
         p1 += 1
      else:
         nums1[p1+1:m+1] = nums1[p1:m]
         nums1[p1] = nums2[p2]
         p1 += 1
         p2 += 1
         m += 1
   if p2 < n:
      nums1[p1:m+n] = nums2[p2:n]
   