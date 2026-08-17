class Solution:
  def longestSubsequence(self, nums: list[int]) -> int:
    if all(x == 0 for x in nums):
      return 0

    total_xor = 0
    for x in nums:
      total_xor ^= x

    return len(nums) if total_xor != 0 else len(nums) - 1