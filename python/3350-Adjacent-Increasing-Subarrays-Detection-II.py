# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        res = 1
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                dp[i] = dp[i - 1] + 1
            
            if i - dp[i] >= 0 and dp[i - dp[i]] >= dp[i]:
                res = max(res, dp[i])

            if not dp[i] & 1 and dp[i - dp[i] // 2] >= dp[i] // 2:
                res = max(res, dp[i - dp[i] // 2])

        return res