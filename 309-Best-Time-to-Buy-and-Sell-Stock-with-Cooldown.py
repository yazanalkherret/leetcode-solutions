# Bottom-up Dynamic Programming
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[0, 0] for _ in range(n + 2)]
        for i in range(n -1, -1, -1):
            dp[i][0] = max(dp[i + 1][1] - prices[i], dp[i + 1][0])
            dp[i][1] = max(dp[i + 2][0] + prices[i], dp[i + 1][1])

        return dp[0][0]

# Top-down Dynamic Programming
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @lru_cache(None)
        def dp(i, holding):
            if i >= n: return 0

            if holding:
                return max(
                    dp(i + 2, 0) + prices[i],
                    dp(i + 1, 1)
                )
            else:
                return max(
                    dp(i + 1, 1) - prices[i],
                    dp(i + 1, 0)
                )

        return dp(0, 0)
