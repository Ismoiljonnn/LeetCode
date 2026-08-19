from collections import Counter

class Solution:
  def largestInteger(self, nums: list[int], k: int) -> int:
    cnt = Counter()
    n = len(nums)

    for i in range(n - k + 1):
      sub_set = set(nums[i : i + k])
      for x in sub_set:
        cnt[x] += 1

    ans = -1
    for x, count in cnt.items():
      if count == 1:
        ans = max(ans, x)

    return ans