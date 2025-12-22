# Bottom-up DP
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m - 1, -1, -1):
            for j in range(n -1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        lcs = dp[0][0]

        return m + n - 2 * lcs

# Top-down DP
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        @lru_cache(None)
        def dp(i, j):
            if i == m or j == n:
                return 0

            if word1[i] == word2[j]:
                return 1 + dp(i + 1, j + 1)
            else:
                return max(dp(i + 1, j), dp(i, j + 1))

        
        lcs = dp(0, 0)

        return m + n - 2 * lcs