class Solution:
  def maxSubarrayLength(self, nums: list[int], k: int) -> int:
    freq = {} 
    left = 0
    max_len = 0

    for right in range(len(nums)):
      val = nums[right]
      freq[val] = freq.get(val, 0) + 1

      while freq[val] > k:
        freq[nums[left]] -= 1
        left += 1

      max_len = max(max_len, right - left + 1)

    return max_len