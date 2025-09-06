# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Current = left + up
                dp[i][j] = max(dp[i][j], dp[i][j - 1] + dp[i - 1][j])
                
        return dp[m][n]