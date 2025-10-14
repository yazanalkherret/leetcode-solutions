# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp[i] += dp[i - 1]
            
            if i - k >= 0 and dp[i] >= k and dp[i - k] >= k:
                return True

        return False