class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        max_l = [[0] * n for _ in range(n)]
        max_r = [[0] * n for _ in range(n)]

        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                total = pref[j + 1] - pref[i]

                k = i
                while (pref[k + 1] - pref[i]) * 2 < total:
                    k += 1

                if (pref[k + 1] - pref[i]) * 2 == total:
                    val = max(max_l[i][k], max_r[k + 1][j])
                else:
                    left_val = max_l[i][k - 1] if k > i else 0
                    right_val = max_r[k + 1][j] if k < j else 0
                    val = max(left_val, right_val)

                dp[i][j] = val
                max_l[i][j] = max(max_l[i][j - 1], val + total)
                max_r[i][j] = max(max_r[i + 1][j], val + total)

        return dp[0][n - 1]