class Solution:
  def longestCommonPrefix(self, strs):
    if not strs:
      return ""

    strs.sort()
    first = strs[0]
    last = strs[-1]
    ans = []

    for i in range(min(len(first), len(last))):
      if first[i] != last[i]:
        break
      ans.append(first[i])

    return "".join(ans)