# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        dp = energy[::]
        n = len(energy)
        ans = -inf
        for i in range(n - 1, -1, -1):
            if i + k < n:
                dp[i] += dp[i + k]
            ans = max(ans, dp[i])

        return ans
        