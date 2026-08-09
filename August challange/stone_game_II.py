class Solution:
  def stoneGameII(self, piles: list[int]) -> int:
    memo = {}
    suffix_sums = piles.copy()
    for i in range(len(piles) - 2, -1, -1):
      suffix_sums[i] += suffix_sums[i + 1]

    def dp(i, m):
      if i >= len(piles):
        return 0
      if (i, m) in memo:
        return memo[(i, m)]

      if i + 2 * m >= len(piles):
        return suffix_sums[i]

      min_stones = float("inf")
      for x in range(1, 2 * m + 1):
        min_stones = min(
          min_stones, dp(i + x, max(m, x))
        )

      memo[(i, m)] = suffix_sums[i] - min_stones
      return memo[(i, m)]

    return dp(0, 1)