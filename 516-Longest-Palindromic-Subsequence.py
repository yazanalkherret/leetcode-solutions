# Bottom-up DP
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [ [0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][-1]

# Top-down DP
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def dp(l, r):
            if r < l: return 0
            if r == l: return 1

            if s[l] == s[r]:
                return 2 + dp(l + 1, r - 1)
            else:
                return max(dp(l + 1, r), dp(l, r - 1))

        return dp(0, len(s) - 1)
