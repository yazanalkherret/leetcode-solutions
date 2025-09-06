# Time Complexity: O(ROWS^2) = O(n), where n is the total number of elements
# Space Complexity: O(ROWS^2) = O(n), where n is the total number of elements

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ROWS = len(triangle)
        dp = [[float("inf")] + row + [float("inf")] for row in triangle]

        for i in range(1, ROWS):
            for j in range(1, i + 2):
                dp[i][j] = dp[i][j] + min(dp[i - 1][j], dp[i - 1][j - 1])

        return min(dp[-1])