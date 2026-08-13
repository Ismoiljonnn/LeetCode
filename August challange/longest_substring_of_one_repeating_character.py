from typing import List

class Solution:
  def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
    n = len(s)
    s_list = list(s)

    tree_max = [0] * (4 * n)
    tree_pref = [0] * (4 * n)
    tree_suff = [0] * (4 * n)
    tree_pchar = [''] * (4 * n)
    tree_schar = [''] * (4 * n)

    def merge(node, l_node, r_node, l_len, r_len):
      tree_pchar[node] = tree_pchar[l_node]
      tree_schar[node] = tree_schar[r_node]

      m = max(tree_max[l_node], tree_max[r_node])

      if tree_schar[l_node] == tree_pchar[r_node]:
        m = max(m, tree_suff[l_node] + tree_pref[r_node])
      tree_max[node] = m

      tree_pref[node] = tree_pref[l_node] + (
        tree_pref[r_node] if tree_pref[l_node] == l_len and tree_pchar[l_node] == tree_pchar[r_node] else 0
      )

      tree_suff[node] = tree_suff[r_node] + (
        tree_suff[l_node] if tree_suff[r_node] == r_len and tree_schar[l_node] == tree_schar[r_node] else 0
      )

    def build(node, l, r):
      if l == r:
        tree_max[node] = 1
        tree_pref[node] = 1
        tree_suff[node] = 1
        tree_pchar[node] = s_list[l]
        tree_schar[node] = s_list[l]
        return

      mid = (l + r) // 2
      left_c, right_c = 2 * node, 2 * node + 1
      build(left_c, l, mid)
      build(right_c, mid + 1, r)
      merge(node, left_c, right_c, mid - l + 1, r - mid)

    def update(node, l, r, idx, char):
      if l == r:
        tree_pchar[node] = char
        tree_schar[node] = char
        return

      mid = (l + r) // 2
      left_c, right_c = 2 * node, 2 * node + 1
      if idx <= mid:
        update(left_c, l, mid, idx, char)
      else:
        update(right_c, mid + 1, r, idx, char)
      merge(node, left_c, right_c, mid - l + 1, r - mid)

    build(1, 0, n - 1)

    ans = []
    for ch, idx in zip(queryCharacters, queryIndices):
      if s_list[idx] != ch:
        s_list[idx] = ch
        update(1, 0, n - 1, idx, ch)
      ans.append(tree_max[1])

    return ans