class Solution:
  def smallestNumber(self, num: str, t: int) -> str:
    temp = t
    c2 = c3 = c5 = c7 = 0
    while temp % 2 == 0: c2 += 1; temp //= 2
    while temp % 3 == 0: c3 += 1; temp //= 3
    while temp % 5 == 0: c5 += 1; temp //= 5
    while temp % 7 == 0: c7 += 1; temp //= 7

    if temp > 1:
      return "-1"

    n = len(num)
    zero_idx = num.find('0')

    DIGIT_FACTORS = {
      '1': (0, 0, 0, 0), '2': (1, 0, 0, 0), '3': (0, 1, 0, 0),
      '4': (2, 0, 0, 0), '5': (0, 0, 1, 0), '6': (1, 1, 0, 0),
      '7': (0, 0, 0, 1), '8': (3, 0, 0, 0), '9': (0, 2, 0, 0),
    }

    pref2, pref3, pref5, pref7 = [0]*(n+1), [0]*(n+1), [0]*(n+1), [0]*(n+1)
    limit = n if zero_idx == -1 else zero_idx
    for k in range(limit):
      d2, d3, d5, d7 = DIGIT_FACTORS[num[k]]
      pref2[k + 1] = pref2[k] + d2
      pref3[k + 1] = pref3[k] + d3
      pref5[k + 1] = pref5[k] + d5
      pref7[k + 1] = pref7[k] + d7

    if zero_idx == -1:
      if pref2[n] >= c2 and pref3[n] >= c3 and pref5[n] >= c5 and pref7[n] >= c7:
        return num

    def min_len_needed(req2, req3, req5, req7):
      req2, req3, req5, req7 = max(0, req2), max(0, req3), max(0, req5), max(0, req7)
      cnt = req7 + req5 + (req3 // 2)
      rem3 = req3 % 2
      cnt += req2 // 3
      rem2 = req2 % 3

      if rem3 == 1 and rem2 > 0:
        cnt += 1
        rem3, rem2 = 0, rem2 - 1

      cnt += rem2 // 2
      rem2 %= 2
      return cnt + rem3 + rem2

    def build_suffix(req2, req3, req5, req7, target_len):
      req2, req3, req5, req7 = max(0, req2), max(0, req3), max(0, req5), max(0, req7)
      d7, d5 = req7, req5
      d9, rem3 = req3 // 2, req3 % 2
      d8, rem2 = req2 // 3, req2 % 3

      d6 = 0
      if rem3 == 1 and rem2 > 0:
        d6 = 1
        rem3, rem2 = 0, rem2 - 1

      d4, rem2 = rem2 // 2, rem2 % 2
      d3, d2 = rem3, rem2

      used_len = d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9
      d1 = target_len - used_len

      return ("1" * d1 + "2" * d2 + "3" * d3 + "4" * d4 + 
              "5" * d5 + "6" * d6 + "7" * d7 + "8" * d8 + "9" * d9)

    max_i = n - 1 if zero_idx == -1 else zero_idx
    for i in range(max_i, -1, -1):
      start_d = int(num[i]) + 1 if i < limit else 1
      p2, p3, p5, p7 = pref2[i], pref3[i], pref5[i], pref7[i]

      for d in range(start_d, 10):
        d2, d3, d5, d7 = DIGIT_FACTORS[str(d)]
        req2, req3, req5, req7 = c2 - p2 - d2, c3 - p3 - d3, c5 - p5 - d5, c7 - p7 - d7

        rem_len = n - 1 - i
        if min_len_needed(req2, req3, req5, req7) <= rem_len:
          return num[:i] + str(d) + build_suffix(req2, req3, req5, req7, rem_len)

    min_l = min_len_needed(c2, c3, c5, c7)
    target_len = max(n + 1, min_l)
    return build_suffix(c2, c3, c5, c7, target_len)