# Time Complexity: O(26n) -> O(n)
# Space Complexity: O(26 + n) -> O(n)

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [1] * n
        lastSeenLongest = [0] * 26

        def ordx(char):
            return ord(char) - ord("a")

        for i in range(n):
            for j in range(max(0, ordx(s[i]) - k), min(26, ordx(s[i]) + k + 1)):
                dp[i] = max(dp[i], 1 + lastSeenLongest[j])
            lastSeenLongest[ordx(s[i])] = max(lastSeenLongest[ordx(s[i])], dp[i])

        return max(dp)