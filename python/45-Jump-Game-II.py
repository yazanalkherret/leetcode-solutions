# Dynamic Programming
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("inf")] * n
        dp[-1] = 0

        for i in range(n - 2, -1, -1):
            for j in range(0, min(n - i, nums[i] + 1)):
                dp[i] = min(dp[i], 1 + dp[i + j])

        return dp[0]
