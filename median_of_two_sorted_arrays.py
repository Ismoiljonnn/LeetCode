class Solution:
  def findMedianSortedArrays(self, nums1, nums2):
    if len(nums1) > len(nums2):
      nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    half_len = (m + n + 1) // 2

    while left <= right:
      i = (left + right) // 2
      j = half_len - i

      nums1LeftMax = nums1[i - 1] if i > 0 else float('-inf')
      nums1RightMin = nums1[i] if i < m else float('inf')

      nums2LeftMax = nums2[j - 1] if j > 0 else float('-inf')
      nums2RightMin = nums2[j] if j < n else float("inf")

      if nums1LeftMax <= nums2RightMin and nums2LeftMax <= nums1RightMin:
        if (m + n) % 2 == 1:
          return max(nums1LeftMax, nums2LeftMax)
        return (max(nums1LeftMax, nums2LeftMax) + min(nums1RightMin, nums2RightMin)) / 2.0
      elif nums1LeftMax > nums2RightMin:
        right = i - 1
      else:
        left = i + 1