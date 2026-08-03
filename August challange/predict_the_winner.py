from typing import List

class Solution:
  def PredictTheWinner(self, nums: List[int]) -> bool:
    memo = {}

    def helper(i, j):
      if i > j:
        return 0
      if i == j:
        return nums[i]
      if (i, j) in memo:
        return memo[(i, j)]

      take_left = nums[i] - helper(i + 1, j)
      take_right = nums[j] - helper(i, j -1)

      memo[(i, j)] = max(take_left, take_right)
      return memo[(i, j)]

    return helper(0, len(nums) - 1) >= 0