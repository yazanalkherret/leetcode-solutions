# Bottom-up DP
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[[0, 0, 0] for _ in range(2)] for _ in range(n + 1)]
        print(dp)
        for i in range(n - 1, -1, -1):
            for r in range(1, 3):
                dp[i][0][r] = max(-prices[i] + dp[i + 1][1][r], dp[i + 1][0][r])
                dp[i][1][r] = max(prices[i] + dp[i + 1][0][r - 1], dp[i + 1][1][r])
        
        return dp[0][0][2]

# Top-down DP
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def dp(i, h, r):
            if i == n or r == 0: return 0

            skip = dp(i + 1, h, r)

            if h:
                return max(prices[i] + dp(i + 1, 0, r - 1), skip)
            else:
                return max(-prices[i] + dp(i + 1, 1, r), skip)

        return dp(0, 0, 2)
