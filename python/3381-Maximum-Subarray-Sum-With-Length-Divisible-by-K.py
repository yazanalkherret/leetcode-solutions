# Dynamic Programming
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0]
        for i in range(n):
            prefix_sum.append(prefix_sum[-1] + nums[i])

        dp = [0] * (n + 1)
        for i in range(k, n + 1):
            segment_sum = prefix_sum[i] - prefix_sum[i - k]
            dp[i] = max(segment_sum, segment_sum + dp[i - k])

        return max(dp[k:])
