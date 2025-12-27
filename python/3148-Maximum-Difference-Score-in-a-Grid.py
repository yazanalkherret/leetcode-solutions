# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [grid[row][::] + [float("-inf")] for row in range(m)]
        dp.append([float("-inf") for _ in range(n + 1)])
        ans = float("-inf")

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                ans = max(ans, dp[i + 1][j] - dp[i][j], dp[i][j + 1] - dp[i][j])
                dp[i][j] = max(dp[i][j], dp[i + 1][j], dp[i][j + 1])

        return ans
