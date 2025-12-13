# Top-down Dynamic Programming
# Time Complexity: O(n * k)
# Space Complexity: O(n * k)

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i, k, holding):
            if i == len(prices) or k == 0:
                return 0

            if holding:
                return max(prices[i] + dp(i + 1, k - 1, False), dp(i + 1, k, holding))
            else:
                return max(dp(i + 1, k, True) - prices[i], dp(i + 1, k, holding))

        return dp(0, k, False)

# Bottom-up Dynamic Programming
# Time Complexity: O(n * k)
# Space Complexity: O(n * k)

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i + 1][j][0], dp[i + 1][j][1] - prices[i])
                dp[i][j][1] = max(dp[i + 1][j][1], dp[i + 1][j - 1][0] + prices[i])
                
        return dp[0][k][0]
