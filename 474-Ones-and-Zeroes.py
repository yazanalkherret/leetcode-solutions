# Time Complexity: O(m * n * l)
# Space Complexity: O(m * n * l)

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        zeroes = []
        ones = []

        for st in strs:
            count_ones, count_zeroes = 0, 0
            for ch in st:
                if ch == "1":
                    count_ones += 1
                else:
                    count_zeroes += 1
            ones.append(count_ones)
            zeroes.append(count_zeroes)

        @lru_cache(None)
        def dp(i, j, k):
            if j < 0 or k < 0:
                return float("-inf")

            if i < 0:
                return 0
            
            return max(dp(i - 1, j, k), dp(i - 1, j - zeroes[i], k - ones[i]) + 1)

        return dp(len(strs) - 1, m, n)
