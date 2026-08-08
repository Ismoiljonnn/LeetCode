from typing import List

class Solution:
  def validSequence(self, word1: str, word2: int) -> List[int]:
    last = [-1] * len(word2)
    i = len(word1) - 1
    j = len(word2) - 1

    while i >= 0 and j >= 0:
      if word1[i] == word2[j]:
        last[j] = i
        j -= 1
      i -= 1

    ans = []
    can_skip = True
    j = 0

    for i in range(len(word1)):
      if j == len(word2):
        break

      if word1[i] == word2[j]:
        ans.append(i)
        j += 1
      elif can_skip and (j == len(word2) - 1 or i < last[j + 1]):
        can_skip = False
        ans.append(i)
        j += 1

    return ans if j == len(word2) else []