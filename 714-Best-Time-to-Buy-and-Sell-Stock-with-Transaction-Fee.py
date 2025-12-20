# Bottom-up DP
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [0, 0]

        for i in range(n - 1, -1, -1):
            dp[0] = max(dp[1] - prices[i], dp[0])
            dp[1] = max(dp[0] + prices[i] - fee, dp[1])

        return dp[0]

# Top-down DP
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        
        @lru_cache(None)
        def dp(i, holding):
            if i == n: return 0

            if not holding:
                return max(dp(i + 1, True) - prices[i], dp(i + 1, False))
            else:
                return max(prices[i] - fee + dp(i + 1, False), dp(i + 1, True))

        return dp(0, False)
