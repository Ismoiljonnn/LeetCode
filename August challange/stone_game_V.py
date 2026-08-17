from functools import cache

class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]
            
        def get_sum(i, j):
            return pref[j + 1] - pref[i]

        @cache
        def dp(i, j):
            if i == j:
                return 0
            
            max_score = 0
            for k in range(i, j):
                left_sum = get_sum(i, k)
                right_sum = get_sum(k + 1, j)
                
                if left_sum < right_sum:
                    max_score = max(max_score, left_sum + dp(i, k))
                elif left_sum > right_sum:
                    max_score = max(max_score, right_sum + dp(k + 1, j))
                else:
                    max_score = max(
                        max_score, 
                        left_sum + dp(i, k), 
                        right_sum + dp(k + 1, j)
                    )
                    
            return max_score

        return dp(0, n - 1)
